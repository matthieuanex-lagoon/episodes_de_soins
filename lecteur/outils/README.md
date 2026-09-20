# Fabriquer un cours

Le Lecteur ne synthétise rien dans le navigateur : il joue des fichiers son
préparés à l'avance. C'est ce qui fait la différence de voix — et c'est aussi
pour ça qu'un nouveau cours demande un passage par ce script.

## Ajouter un cours

1. Écrire `lecteur/documents/<identifiant>.txt` :

   ```
   titre: Bilan Act 2
   matiere: SVT — La théorie cellulaire
   langue: fr
   voix: fr_FR-siwis-medium
   ---
   Premier paragraphe.

   Deuxième paragraphe. Les phrases sont découpées automatiquement.

   – une ligne commençant par un tiret cadratin devient une puce.
   ```

   `voix` est facultatif ; à défaut, `fr_FR-siwis-medium` en français et
   `en_GB-jenny_dioco-medium` en anglais.

2. Lancer la fabrique :

   ```
   pip install piper-tts lameenc
   python3 lecteur/outils/fabrique.py bilan-act-2    # ou rien, pour tout refaire
   ```

Elle écrit `lecteur/audio/<identifiant>.mp3`, le minutage
`lecteur/audio/<identifiant>.json`, et réinjecte l'ensemble dans
`lecteur/index.html` entre les repères `/* <<< DOCUMENTS */` et
`/* DOCUMENTS >>> */`. Ne pas modifier ce bloc à la main.

## Les voix

Modèles [Piper](https://github.com/rhasspy/piper), synthèse neuronale locale.
Ils ne sont pas versionnés — environ 60 Mo pièce — et se téléchargent depuis
`huggingface.co/rhasspy/piper-voices` vers le dossier pointé par `VOIX_DIR`
(`/home/user/voix` par défaut) :

| Voix | Langue | Remarque |
|------|--------|----------|
| `fr_FR-siwis-medium` | français | voix de femme, celle en service |
| `fr_FR-upmc-medium` | français | voix de femme, autre timbre |
| `fr_FR-tom-medium` | français | voix d'homme, 44,1 kHz |
| `en_GB-jenny_dioco-medium` | anglais | voix de femme, accent britannique |

```
curl -sSL -o "$VOIX_DIR/fr_FR-siwis-medium.onnx" \
  https://huggingface.co/rhasspy/piper-voices/resolve/main/fr/fr_FR/siwis/medium/fr_FR-siwis-medium.onnx
curl -sSL -o "$VOIX_DIR/fr_FR-siwis-medium.onnx.json" \
  https://huggingface.co/rhasspy/piper-voices/resolve/main/fr/fr_FR/siwis/medium/fr_FR-siwis-medium.onnx.json
```

## Deux réglages qui comptent

`ALLONGEMENT` en tête du script ralentit la diction à la source (1,06 : un peu
plus posé que le réglage d'usine). Il vaut mieux corriger là que dans le
lecteur : la vitesse du lecteur étire un enregistrement, elle ne change pas la
façon de dire.

`LEXIQUE_FR` réécrit phonétiquement les noms propres que la voix française
écorche — Leeuwenhoek, Janssen, Schleiden. Le texte affiché reste intact :
seule la prononciation est corrigée. Tout nom étranger d'un nouveau cours est
à vérifier à l'oreille et, au besoin, à ajouter là.
