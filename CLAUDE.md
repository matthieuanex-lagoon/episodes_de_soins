# CLAUDE.md — Épisodes de soins

Proposition d'ergonomie pour le module **« Episodes et suivis en cours »** d'un logiciel de dossier médical français (XMED, IHM DevExpress WinForms). Ce dépôt contient des documents de conception, pas de code applicatif.

## Objectif

> **Voir d'emblée ce qui doit être priorisé et important.**

Le cadre trie aujourd'hui par libellé ou par date — deux critères sans information clinique. On ajoute un niveau **importance du suivi** à trois valeurs, rendu par trois petits carrés, et on trie dessus.

## Contraintes du produit — non négociables

- **Rien n'est attribué par la machine.** À la création d'un épisode, la colonne est vide et le reste jusqu'à décision du praticien. Ni déduction depuis le CIM10 / CISP / ALD / « À suivre », ni proposition pré-remplie à valider, **même si une règle paraît logique sur le moment**. Ce point a été tranché explicitement après avoir été rediscuté : ne pas le rouvrir sans demande.
- **Le logiciel n'utilise pas le clic droit.** Aucune solution ne peut reposer sur un menu contextuel. La multi-sélection se traite par la touche appliquée aux lignes sélectionnées.
- **Le rouge du libellé appartient à l'ALD** (`#C00000`). L'importance ne s'exprime jamais par la couleur du texte.
- **Le compte de carrés 3 / 2 / 1 n'est pas décoratif.** Rouge/orange/vert est l'axe qu'une deutéranopie ne distingue pas (~8 % des hommes), et le compte est la seule information qui survive à l'impression noir et blanc du module.

## Vocabulaire — arrêté avec Sophie (équipe dev)

- Le champ s'appelle **Importance**, jamais « Priorité ».
- Valeurs **haute / moyenne / basse**, jamais 1-2-3, jamais P1/P2/P3. Les chiffres n'existent que comme raccourcis clavier.
- Écrire **« importance du suivi »** en toutes lettres où la place le permet : « importance » seul dérive vers l'importance de la maladie, lecture que la proposition écarte.

## Sémantique — le piège principal

Le niveau mesure la **charge de surveillance actuelle**, pas la gravité intrinsèque. Un cancer en rémission redescend ; une sciatique aiguë reste en bas. Et surtout : **l'incertitude élève le niveau au même titre que la gravité** — un nodule pulmonaire sans précision n'est pas un diagnostic grave, c'est un diagnostic absent, et c'est pour ça qu'il est haut. C'est le point le plus facile à aplatir en résumant.

## Rendu

Gouttière de 32 px à l'extrême gauche, fond gris conservé même sur ligne sélectionnée, mais triable au clic. Trois carrés de 7 px espacés de 2 px : haute `#D33A2C`, moyenne `#DB7500`, basse `#2E8B45`, emplacements non atteints `#DCDCDC`. Colonne entièrement vide si aucun niveau n'est posé — ne jamais la confondre visuellement avec un niveau bas.

Trois représentations ont été étudiées puis écartées : barre verticale segmentée, feu tricolore remplaçant « À suivre », rang manuel. Elles restent documentées avec leur maquette dans `index.html` §02 — **ne pas les supprimer**, elles portent l'historique des arbitrages.

## Fichiers

| Fichier | Rôle |
|---------|------|
| `index.html` | La maquette publiée, servie par GitHub Pages à la racine. **Ne pas renommer** : l'URL Pages et celle de l'artifact Claude sont liées à ce chemin. |
| `Modele-priorite-suivi.md` | La même proposition en texte, lisible en diff. |
| `README.md` | Porte d'entrée du dépôt. |

Les trois se tiennent : une décision changée doit l'être dans les trois.

## Identité visuelle de `index.html`

Reprise **exacte** du design de la maquette Prévention (`matthieuanex-lagoon.github.io/maquette-prevention/`), pour que les deux documents forment une série :

- Tokens : `--paper #f6f4f0`, `--ink #22201d`, `--ink-soft #5c5751`, `--rule #ddd8d0`, `--card #ffffff`, `--accent #9c3d2a`, `--accent-soft #f3e7e3`.
- Georgia pour les titres, sans-serif système pour le texte. Page mono-thème, sans mode sombre : choix de série, pas oubli.
- Structure : `header.top` collant, `.hero` + `.phases` + `.version`, sections numérotées `.sec-num` / `h2`, `blockquote` pour la thèse, `.shots` / `.shot` / `figcaption` pour les maquettes, `.essayez` pour l'interactif, `.hint` en italique, `table.decisions` pour les tableaux.
- Les maquettes d'IHM utilisent le vocabulaire `.wf` (WinForms) de la page Prévention.

Ne pas y réintroduire de mode sombre ni d'autre famille typographique.

## La grille de la section 03 est manipulable

Un composant en fin de fichier la pilote. Contrat DOM à respecter si l'on touche au balisage :

- conteneur `.grille` avec `tabindex="0"` ; lignes `.grow` portant `data-imp` (`1|2|3`, `0` = aucune), `data-lib`, `data-deb` (ISO) ;
- cellule `.k-i` — **contenu rendu par le script**, ne rien y écrire en dur ; `.k-dc` porte le dernier contact au format `jj/mm/aaaa` (clé de tri secondaire) ;
- `.statut` en frère de `.grille` dans `.win` ; chips `[data-tri="imp|lib|deb"]` et bouton `[data-action="retrier"]` dans la même `<figure>`.

Comportements implémentés, qui sont autant d'assertions de la proposition : clic en trois zones avec aperçu au survol, re-clic du niveau actif qui l'efface, `1` `2` `3` `0` au clavier, `Ctrl+Z`, compteur vivant, **absence de re-tri pendant l'édition** avec bouton « Réappliquer le tri », réinitialisation par le lien de la barre de navigation.

Ne pas dupliquer d'identifiant : les lignes vivent dans `#grille-lignes`.

## Données d'exemple — le dépôt est public

Dépôt `matthieuanex-lagoon/episodes_de_soins`, **public**, avec Pages actif. Le dossier d'exemple est dérivé d'un cas réel : libellés cliniques, codes CIM10 et niveaux conservés parce qu'ils font la valeur de la démonstration ; **jours et mois des dates de début décalés, notes libres généralisées**.

Avant tout commit, vérifier qu'aucune donnée patient verbatim n'a été réintroduite — l'historique git ne se purge pas.

## Publication

- **GitHub Pages** : https://matthieuanex-lagoon.github.io/episodes_de_soins/ (branche `main`, dossier racine).
- L'artifact Claude se met à jour en republiant le même chemin de fichier.
- Pas de `gh` CLI sur cette machine ; le credential manager Windows porte les accès GitHub. Commits rédigés en français.

## État des arbitrages

| Sujet | État |
|-------|------|
| Représentation, vocabulaire, saisie, tri | Arrêtés |
| Coloration rouge du libellé ALD | **Ouvert** |
| Recouvrement avec la case « À suivre » | **Ouvert** |
| Vieillissement des niveaux | **À étudier** — porterait sur la cellule `Dernier contact`, jamais sur les carrés |
