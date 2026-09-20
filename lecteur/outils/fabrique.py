#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fabrique les fichiers son du Lecteur.

Chaque document est un fichier texte de lecteur/documents/ portant un petit
en-tete. On en sort un MP3 et un bloc de minutage : le Lecteur surligne la
phrase dite parce qu'il connait la seconde ou chacune commence.

    python3 lecteur/outils/fabrique.py                  # tout
    python3 lecteur/outils/fabrique.py bilan-act-2      # un seul document

Les voix sont des modeles Piper (.onnx) places dans VOIX_DIR. Elles ne sont
pas versionnees : ~60 Mo piece. Voir lecteur/outils/README.md.
"""

import json
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(RACINE, "documents")
AUDIO_DIR = os.path.join(RACINE, "audio")
VOIX_DIR = os.environ.get("VOIX_DIR", "/home/user/voix")

VOIX_DEFAUT = {"fr": "fr_FR-siwis-medium", "en": "en_GB-jenny_dioco-medium"}

# Un peu plus lent que le reglage d'usine : c'est une lecon, pas un journal.
ALLONGEMENT = 1.06
# Silences, en secondes. Une phrase respire ; un paragraphe respire plus.
PAUSE_PHRASE = 0.28
PAUSE_BLOC = 0.55
PAUSE_TITRE = 0.70
DEBIT_MP3 = 64


# --------------------------------------------------------------------------
# Decoupage en phrases : meme regle que celle affichee par le Lecteur.
# --------------------------------------------------------------------------
ABREV = re.compile(
    r"(?:\b(?:M|MM|Mme|Mlle|Dr|Pr|St|Ste|etc|cf|ex|env|av|ap|ref|fig|p|vol|Mr|Mrs|Ms|Jr|Sr|vs)"
    r"|\b[A-ZÀ-Þ])\.$"
)


def decouper_phrases(t):
    out, cur, i = [], "", 0
    while i < len(t):
        cur += t[i]
        if t[i] in ".!?…":
            while i + 1 < len(t) and t[i + 1] in "\"'»)]”’":
                i += 1
                cur += t[i]
            suite = t[i + 1:]
            m = re.match(r"^[ \t]+", suite)
            if m:
                apres = suite[len(m.group(0)):len(m.group(0)) + 1]
                if (apres and not ABREV.search(cur.strip())
                        and re.match(r"[A-ZÀ-ÖØ-Þ«\"“'(\d–—-]", apres)):
                    out.append(cur.strip())
                    cur = ""
                    i += len(m.group(0))
        i += 1
    if cur.strip():
        out.append(cur.strip())
    return out or [t.strip()]


# --------------------------------------------------------------------------
# Prononciation : ce que le francais ecrit d'une facon et se dit d'une autre.
# --------------------------------------------------------------------------
ORDINAUX = {
    1: "premier", 2: "deuxième", 3: "troisième", 4: "quatrième",
    5: "cinquième", 6: "sixième", 7: "septième", 8: "huitième",
    9: "neuvième", 10: "dixième", 11: "onzième", 12: "douzième",
    13: "treizième", 14: "quatorzième", 15: "quinzième",
    16: "seizième", 17: "dix-septième", 18: "dix-huitième",
    19: "dix-neuvième", 20: "vingtième", 21: "vingt-et-unième",
}

# Noms propres que Piper prononce a la francaise alors qu'ils ne le sont pas.
LEXIQUE_FR = {
    "Leeuwenhoek": "Leûweun'houk",
    "Janssen": "Yanne-seune",
    "Schleiden": "Chlaïdeune",
    "Schwann": "Chvane",
    "Hook": "Houk",
    "Remake": "Remak",
}


def pour_la_voix(t, lang):
    s = re.sub(r"^\s*[–—-]\s*", "", t)
    if lang == "fr":
        s = re.sub(r"(\d{1,2})\s*(?:ème|eme|e)\b",
                   lambda m: ORDINAUX.get(int(m.group(1)), m.group(1) + "ième"), s)
        s = re.sub(r"(\d+)\s*x(?![a-zA-Zà-ÿ])", r"\1 fois", s)
        for mot, dit in LEXIQUE_FR.items():
            s = re.sub(r"\b" + re.escape(mot) + r"\b", dit, s)
    s = re.sub(r"[«»“”]", "", s)
    return s.strip() or t


# --------------------------------------------------------------------------
# Lecture d'un document source
# --------------------------------------------------------------------------
def lire_document(chemin):
    brut = open(chemin, encoding="utf-8").read()
    if "\n---\n" not in brut:
        raise SystemExit("%s : en-tete manquant (ligne --- attendue)" % chemin)
    tete, corps = brut.split("\n---\n", 1)
    meta = {}
    for ligne in tete.strip().splitlines():
        if ":" in ligne:
            k, v = ligne.split(":", 1)
            meta[k.strip()] = v.strip()

    blocs = []
    for para in re.split(r"\n\s*\n", corps.strip()):
        texte = re.sub(r"\s*\n\s*", " ", para).strip()
        if not texte:
            continue
        blocs.append({"type": "li" if re.match(r"^[–—-]\s", texte) else "p",
                      "texte": texte})
    meta["blocs"] = blocs
    meta.setdefault("langue", "fr")
    meta.setdefault("matiere", "")
    meta["id"] = os.path.splitext(os.path.basename(chemin))[0]
    return meta


# --------------------------------------------------------------------------
# Fabrication
# --------------------------------------------------------------------------
def fabriquer(meta):
    from piper import PiperVoice, SynthesisConfig
    import lameenc

    lang = meta["langue"]
    nom_voix = meta.get("voix") or VOIX_DEFAUT[lang]
    modele = os.path.join(VOIX_DIR, nom_voix + ".onnx")
    if not os.path.exists(modele):
        raise SystemExit("Voix absente : %s\nVoir lecteur/outils/README.md" % modele)

    voix = PiperVoice.load(modele)
    cfg = SynthesisConfig(length_scale=ALLONGEMENT, noise_scale=0.667,
                          noise_w_scale=0.8, normalize_audio=True)

    pcm = bytearray()
    taux = None
    phrases = []

    def silence(secondes):
        pcm.extend(b"\x00\x00" * int(taux * secondes))

    # Le titre dit en ouverture : on sait ce qu'on ecoute avant que ca commence.
    ouverture = meta["titre"] + ("." if not meta["titre"].endswith(".") else "")
    morceaux_titre = list(voix.synthesize(pour_la_voix(ouverture, lang), syn_config=cfg))
    taux = morceaux_titre[0].sample_rate
    for m in morceaux_titre:
        pcm.extend(m.audio_int16_bytes)
    silence(PAUSE_TITRE)

    for ib, bloc in enumerate(meta["blocs"]):
        for ph in decouper_phrases(bloc["texte"]):
            debut = len(pcm) / 2 / taux
            for m in voix.synthesize(pour_la_voix(ph, lang), syn_config=cfg):
                pcm.extend(m.audio_int16_bytes)
            fin = len(pcm) / 2 / taux
            phrases.append({"t": ph, "b": ib, "k": bloc["type"],
                            "d": round(debut, 3), "f": round(fin, 3)})
            silence(PAUSE_PHRASE)
        silence(PAUSE_BLOC - PAUSE_PHRASE)

    duree = len(pcm) / 2 / taux

    enc = lameenc.Encoder()
    enc.set_bit_rate(DEBIT_MP3)
    enc.set_in_sample_rate(taux)
    enc.set_channels(1)
    enc.set_quality(2)
    mp3 = enc.encode(bytes(pcm)) + enc.flush()

    os.makedirs(AUDIO_DIR, exist_ok=True)
    chemin_mp3 = os.path.join(AUDIO_DIR, meta["id"] + ".mp3")
    open(chemin_mp3, "wb").write(mp3)

    fiche = {
        "id": meta["id"],
        "titre": meta["titre"],
        "matiere": meta["matiere"],
        "langue": lang,
        "voix": nom_voix,
        "duree": round(duree, 2),
        "mots": sum(len(b["texte"].split()) for b in meta["blocs"]),
        "audio": "audio/%s.mp3" % meta["id"],
        "phrases": phrases,
    }
    open(os.path.join(AUDIO_DIR, meta["id"] + ".json"), "w", encoding="utf-8").write(
        json.dumps(fiche, ensure_ascii=False, indent=1))

    print("%-16s %5.1f s  %6.0f ko  %3d phrases  (%s)"
          % (meta["id"], duree, len(mp3) / 1024, len(phrases), nom_voix))
    return fiche


def injecter(fiches):
    """Ecrit les fiches dans index.html, entre les deux reperes."""
    page = os.path.join(RACINE, "index.html")
    s = open(page, encoding="utf-8").read()
    ouvre, ferme = "/* <<< DOCUMENTS */", "/* DOCUMENTS >>> */"
    if ouvre not in s or ferme not in s:
        print("index.html : reperes DOCUMENTS absents, rien d'injecte.")
        return
    bloc = "var DOCS = " + json.dumps(fiches, ensure_ascii=False, indent=1) + ";"
    avant, reste = s.split(ouvre, 1)
    _, apres = reste.split(ferme, 1)
    open(page, "w", encoding="utf-8").write(
        avant + ouvre + "\n" + bloc + "\n" + ferme + apres)
    print("index.html : %d document(s) injecte(s)." % len(fiches))


def main():
    voulus = sys.argv[1:]
    fichiers = sorted(f for f in os.listdir(DOCS_DIR) if f.endswith(".txt"))
    if voulus:
        fichiers = [f for f in fichiers if os.path.splitext(f)[0] in voulus]
        if not fichiers:
            raise SystemExit("Aucun document ne correspond a : %s" % ", ".join(voulus))

    fiches = []
    for f in fichiers:
        fiches.append(fabriquer(lire_document(os.path.join(DOCS_DIR, f))))

    # Les documents non regeneres gardent leur fiche deja calculee.
    if voulus:
        deja = []
        for f in sorted(os.listdir(AUDIO_DIR)):
            if f.endswith(".json"):
                fiche = json.load(open(os.path.join(AUDIO_DIR, f), encoding="utf-8"))
                if fiche["id"] not in [x["id"] for x in fiches]:
                    deja.append(fiche)
        fiches = sorted(fiches + deja, key=lambda x: x["id"])

    injecter(fiches)


if __name__ == "__main__":
    main()
