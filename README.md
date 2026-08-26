# Épisodes de soins — importance du suivi

Spécification d'une évolution du module **« Episodes et suivis en cours »** : donner à chaque épisode un niveau d'importance du suivi, le rendre lisible d'un coup d'œil, et trier dessus.

> **Voir d'emblée ce qui doit être priorisé et important.**

## Le problème

Le cadre n'est pas mal trié — il est trié sur des critères qui **ne portent aucune information clinique**. L'ordre alphabétique classe sur la première lettre d'un libellé ; l'ordre chronologique, sur le moment où quelqu'un a ouvert une ligne. Ni l'un ni l'autre ne dit ce qui doit être revu.

Sur le dossier d'exemple, onze épisodes :

- **Sciatique** et **nodule pulmonaire sans précision** ont été ouverts le même jour. Voisins en tri chronologique, voisins en tri alphabétique, deux lignes noires identiques. L'une se résoudra seule, l'autre est une incertitude à lever.
- L'**artériopathie oblitérante** revascularisée, sous surveillance semestrielle, tombe en huitième position au tri par date — parce qu'elle a été ouverte en 2002.
- L'**insuffisance mitrale** n'a plus été touchée depuis 2011, et rien ne le signale.

## Ce qui est proposé

- **Trois niveaux** — haute, moyenne, basse, plus un état « non définie » de plein droit.
- Le niveau mesure la **charge de surveillance actuelle**, pas la gravité intrinsèque. Il est donc mutable dans le temps.
- **L'incertitude élève le niveau autant que la gravité.** Un nodule pulmonaire sans précision n'est pas un diagnostic grave, c'est un diagnostic absent — et c'est pour cela qu'il passe en haut.
- **Saisie 100 % manuelle** : aucune déduction depuis le CIM10, l'ALD ou les cases existantes. Le nodule pulmonaire du dossier d'exemple n'a ni code, ni note, ni ALD ; aucune règle automatique ne l'aurait trouvé.
- **Rendu par trois petits carrés** dans une gouttière de 32 px à gauche de la ligne — 3 rouges, 2 orange, 1 vert, emplacements non atteints en gris. Aucun chiffre affiché nulle part.
- **Tri** par importance dans le cadre compact, tri mémorisé dans la vue détaillée.

## Fichiers

## La maquette

**→ [matthieuanex-lagoon.github.io/episodes_de_soins](https://matthieuanex-lagoon.github.io/episodes_de_soins/)**

Maquette d'intention avec les écrans avant / après, une démonstration interactive des trois ordres de tri, et l'étayage de chaque décision. Même forme que la [maquette Prévention](https://matthieuanex-lagoon.github.io/maquette-prevention/).

| Fichier | Contenu |
|---------|---------|
| [`index.html`](index.html) | La maquette publiée. Page autonome, ouvrable aussi en local. |
| [`Modele-priorite-suivi.md`](Modele-priorite-suivi.md) | La même spécification en texte : problème, sémantique, dossier d'exemple épisode par épisode, codage visuel, saisie, modèle de données, tri, migration. |
| [`CLAUDE.md`](CLAUDE.md) | Conventions du projet : vocabulaire arrêté, règles de rendu non négociables, état des arbitrages. |

## Deux points restent à trancher

1. **Le rouge est déjà pris par l'ALD** (libellé rouge `#C00000`). Les deux signaux cohabitent parce qu'ils n'occupent ni la même zone, ni la même forme, ni la même teinte. Le dossier d'exemple montre d'ailleurs qu'ils ne sont pas substituables : une ligne rouge et haute, une rouge et moyenne, une noire et haute coexistent dans le même écran. Voir §4.
2. **Recouvrement avec la case « À suivre »**, cochée sur trois épisodes du dossier — mais pas sur les deux qui sont le plus à suivre. Voir §9.

## À l'attention de l'implémentation

Le **compte de carrés 3 / 2 / 1 n'est pas décoratif**. Rouge, orange et vert forment exactement l'axe qu'une deutéranopie ne distingue pas (~8 % des hommes), et c'est aussi la seule information qui survit à l'impression noir et blanc du module. Trois carrés pleins de couleurs différentes feraient perdre les deux garde-fous d'un coup.

---

Le dossier d'exemple est dérivé d'un cas réel : libellés, codes et niveaux conservés, jours et mois des dates de début décalés, notes libres généralisées.
