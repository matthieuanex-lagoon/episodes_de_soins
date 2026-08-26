# Épisodes de soins — importance du suivi

Proposition d'ergonomie pour le module **« Episodes et suivis en cours »** : donner à chaque épisode un niveau d'importance du suivi, le rendre lisible d'un coup d'œil, et trier dessus.

> **Voir d'emblée ce qui doit être priorisé et important.**

## La maquette

**→ [matthieuanex-lagoon.github.io/episodes_de_soins](https://matthieuanex-lagoon.github.io/episodes_de_soins/)**

Les quatre représentations étudiées côte à côte, la grille manipulable, et les points restant à trancher. Même forme que la [maquette Prévention](https://matthieuanex-lagoon.github.io/maquette-prevention/).

## Le problème

Le cadre n'est pas mal trié — il est trié sur des critères qui **ne portent aucune information clinique**. Sur le dossier d'exemple, sciatique et nodule pulmonaire, ouverts le même jour, occupent deux lignes rigoureusement identiques : l'une se résoudra seule, l'autre est une incertitude à lever.

Le tri par la case « À suivre » est le contournement que l'usage a déjà produit. Un drapeau binaire crée un bloc de tête sans hiérarchie interne, et le bloc grossit jusqu'à ne plus rien dire.

## Principes actés

- **Rien n'est attribué par la machine.** À la création, la colonne est vide et le reste jusqu'à décision du praticien. Aucune déduction depuis le CIM10, l'ALD ou les cases existantes, et aucune proposition pré-remplie.
- **Le logiciel n'utilise pas le clic droit** : aucune solution ne repose sur un menu contextuel.
- **Vocabulaire arrêté** : « Importance », haute / moyenne / basse, aucun chiffre affiché.

## Ce qui est proposé

Trois petits carrés dans une gouttière de 32 px à gauche de la ligne — 3 rouges, 2 orange, 1 vert, emplacements non atteints en gris. La gouttière est cliquable en trois zones et triable au clic. Saisie aussi au clavier (`1` `2` `3` `0`, y compris sur une sélection multiple) et depuis le panneau de détail.

Trois autres représentations ont été étudiées et écartées — barre verticale segmentée, feu tricolore remplaçant « À suivre », rang manuel — chacune avec sa maquette et son verdict dans le document.

## Fichiers

| Fichier | Contenu |
|---------|---------|
| [`index.html`](index.html) | La maquette publiée. Page autonome, ouvrable aussi en local. |
| [`Modele-priorite-suivi.md`](Modele-priorite-suivi.md) | La même proposition en texte. |
| [`CLAUDE.md`](CLAUDE.md) | Conventions du projet : principes actés, règles de rendu non négociables, état des arbitrages. |

## À l'attention de l'implémentation

Le **compte de carrés 3 / 2 / 1 n'est pas décoratif**. Rouge, orange et vert forment exactement l'axe qu'une deutéranopie ne distingue pas (~8 % des hommes), et c'est aussi la seule information qui survit à l'impression noir et blanc du module.

---

Le dossier d'exemple est dérivé d'un cas réel : libellés, codes CIM10 et niveaux conservés, jours et mois des dates de début décalés, notes libres généralisées.
