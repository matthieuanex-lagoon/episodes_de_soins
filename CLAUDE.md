# CLAUDE.md — Épisodes de soins

Spécifications d'évolution du module **« Episodes et suivis en cours »** d'un logiciel de dossier médical français (XMED, IHM DevExpress WinForms). Ce dépôt contient des documents de conception, pas de code applicatif.

## Objectif du travail en cours

> **Voir d'emblée ce qui doit être priorisé et important.**

Le cadre des épisodes trie aujourd'hui par libellé ou par date — deux critères sans information clinique, qui mettent tout au même niveau. On ajoute un champ **importance du suivi** à trois niveaux, rendu par trois petits carrés tricolores, et on trie dessus.

## Fichiers

| Fichier | Rôle |
|---------|------|
| `index.html` | La maquette d'intention publiée : le document de référence pour les développeurs et les décideurs. Servi par GitHub Pages à la racine du dépôt — **ne pas renommer**, et l'URL de l'artifact Claude est liée à ce chemin. |
| `Modele-priorite-suivi.md` | La spécification en texte : même contenu, format lisible en diff. |
| `README.md` | Porte d'entrée du dépôt. |

Les trois se tiennent : une décision changée doit l'être dans les trois, sinon elles divergent.

## Identité visuelle de `index.html`

La page reprend **exactement** le design de la maquette Prévention (`matthieuanex-lagoon.github.io/maquette-prevention/`), pour que les deux documents forment une série :

- Tokens : `--paper #f6f4f0`, `--ink #22201d`, `--ink-soft #5c5751`, `--rule #ddd8d0`, `--card #ffffff`, `--accent #9c3d2a`, `--accent-soft #f3e7e3`.
- Georgia pour les titres, sans-serif système pour le texte. Page mono-thème, sans mode sombre : c'est un choix de série, pas un oubli.
- Structure : `header.top` collant avec nav d'ancres, `.hero` + `.phases` + `.version`, sections numérotées `.sec-num` / `h2`, `blockquote` pour la thèse, `.shots` / `.shot` / `figcaption` pour les comparaisons avant-après, `.essayez` pour les zones interactives, `.hint` en italique, `table.decisions` pour les arbitrages.
- Les maquettes d'IHM utilisent le vocabulaire `.wf` (WinForms) de la page Prévention : `.win`, `.grouper`, `.ghead`, `.grow`, `.box`.

Toute reprise de la page doit rester dans ce système. Ne pas y réintroduire de mode sombre ni d'autre famille typographique.

## La maquette est fonctionnelle

Deux grilles sont réellement manipulables — celle de la section 02 (dossier validé, on trie) et celle de la section 05 (première ouverture, tout est proposé). Un seul composant les pilote, en fin de fichier. Contrat DOM à respecter si l'on touche au balisage :

- conteneur `.grille` avec `tabindex="0"` ; lignes `.grow` portant `data-imp` (`1|2|3`, `0` = aucune), `data-valide` (`0|1`, défaut 1), `data-lib`, `data-deb` (ISO) ;
- cellule `.k-i` — son contenu est **rendu par le script**, ne rien y écrire en dur ; `.k-dc` porte le dernier contact au format `jj/mm/aaaa` ;
- `.statut` en frère de `.grille` dans `.win` ; chips de tri `[data-tri="imp|lib|deb"]` et bouton `[data-action="retrier"]` dans la même `<figure>`.

Comportements implémentés, qui sont autant d'assertions de la spec : clic en trois zones avec aperçu au survol, re-clic du niveau actif qui le retire, `1` `2` `3` `0` au clavier, `Ctrl+Z`, péremption recalculée (haute > 6 mois, moyenne > 18 mois, sur les lignes validées seulement), compteur vivant, **absence de re-tri pendant l'édition** avec bouton « Réappliquer le tri », et réinitialisation par le lien de la barre de navigation.

Ne pas dupliquer d'identifiant : `#grille` désigne la section (ancre de nav), les lignes vivent dans `#grille-lignes`.

## Vocabulaire — arrêté, ne pas dériver

- Le champ s'appelle **Importance**, jamais « Priorité » (arbitré avec Sophie, équipe dev).
- Les valeurs sont **haute / moyenne / basse**, jamais 1-2-3, jamais P1/P2/P3.
- Écrire **« importance du suivi »** en toutes lettres partout où la place le permet. « Importance » seul dérive vers l'importance de la maladie, exactement la lecture que la spec écarte.
- Les chiffres 1/2/3 n'existent qu'en base (tri) et comme raccourcis clavier. Ils ne s'affichent nulle part.

## Sémantique — le piège principal

Le niveau mesure la **charge de surveillance actuelle**, pas la gravité intrinsèque de la pathologie. Conséquences à ne jamais perdre en réécrivant :

- Un cancer en rémission redescend de niveau. Une sciatique aiguë reste en bas.
- **L'incertitude élève le niveau au même titre que la gravité.** Un nodule pulmonaire sans précision n'est pas un diagnostic grave, c'est un diagnostic absent — et c'est pour ça qu'il est haut. C'est le point le plus important du document et le plus facile à aplatir en le résumant.

## Règles de rendu — non négociables

- **Le rouge du libellé appartient à l'ALD** (`#C00000`). L'importance ne s'exprime jamais par la couleur du texte.
- Les carrés vivent dans une **gouttière de 32 px** à l'extrême gauche, au fond gris conservé même sur ligne sélectionnée, mais **triable au clic**.
- Couleurs : haute `#D33A2C`, moyenne `#DB7500`, basse `#2E8B45`, emplacements non atteints `#DCDCDC`.
- **Le compte de carrés 3/2/1 n'est pas décoratif.** Rouge/orange/vert est l'axe qu'une deutéranopie ne distingue pas (~8 % des hommes), et le compte est la seule information qui survive à l'impression noir et blanc du module. Trois carrés pleins de couleurs différentes feraient perdre les deux garde-fous d'un coup.
- Ligne **non définie** : colonne entièrement vide, pas même les carrés gris. Ne pas la confondre visuellement avec un niveau bas.

## Données d'exemple — le dépôt est public

Le dépôt GitHub `matthieuanex-lagoon/episodes_de_soins` est **public**. Le dossier d'exemple est dérivé d'un cas réel : libellés cliniques, codes CIM10 et niveaux conservés parce qu'ils font la valeur de la démonstration ; **jours et mois des dates de début décalés, notes libres généralisées**.

Avant tout commit, vérifier qu'aucune donnée patient verbatim n'a été réintroduite — l'historique git ne se purge pas.

## Publication

- **GitHub Pages** sert `index.html` à la racine : https://matthieuanex-lagoon.github.io/episodes_de_soins/ (à activer dans Settings → Pages, branche `main`, dossier `/`).
- L'artifact Claude se met à jour en republiant **le même chemin de fichier** ; changer le nom crée un artifact distinct, sauf à passer l'URL existante en paramètre.
- Le dépôt se met à jour par `git push` sur `main`. Pas de `gh` CLI sur cette machine ; le credential manager Windows porte les accès GitHub.
- Les commits sont rédigés en français.

## État des arbitrages

| Sujet | État |
|-------|------|
| Sémantique, vocabulaire, encodage, tri | Arrêtés |
| Saisie du niveau — deux pistes étudiées (feux cliquables / rang manuel) | **Recommandé** : gouttière cliquable en trois zones, qui remplace « À suivre ». Le rang manuel est écarté ; sa part utile est une épingle, versée aux suites. |
| Coloration rouge du libellé ALD — la garder ou la libérer | **Ouvert**, à décider après usage réel |
| Recouvrement avec la case « À suivre » | **En voie de résolution** : la gouttière cliquable la remplace au lieu de cohabiter avec elle |
| Niveaux de TIPMP, Surveillance coloscopique, Tabagisme | **Proposés**, à valider par le praticien |
