# Épisodes de soins — importance du suivi

Spécification d'une évolution du module **« Episodes et suivis en cours »** : classer les épisodes d'un dossier par importance du suivi, et rendre ce classement lisible d'un coup d'œil dans la grille.

## Le problème

Le cadre classe aujourd'hui par ordre alphabétique. Une exploration ouverte cette semaine arrive donc après un certificat de sport délivré il y a deux ans. Rien, dans la vue, ne dit ce qui demande une action.

## Ce qui est proposé

- **Trois niveaux** — haute, moyenne, basse, plus un état « non définie » de plein droit.
- Le niveau mesure l'**importance du suivi** (charge de surveillance actuelle), pas la gravité intrinsèque de la pathologie. Il est donc mutable dans le temps.
- **Saisie 100 % manuelle** : aucune déduction depuis le CIM10, l'ALD ou les cases existantes.
- **Rendu par trois petits carrés** dans une gouttière de 32 px à gauche de la ligne — 3 rouges, 2 orange, 1 vert, emplacements non atteints en gris. Aucun chiffre affiché nulle part.
- **Tri** par importance dans le cadre compact, tri mémorisé dans la vue détaillée.

## Fichiers

| Fichier | Contenu |
|---------|---------|
| [`Modele-priorite-suivi.md`](Modele-priorite-suivi.md) | La spécification : sémantique, codage visuel, saisie, modèle de données, tri, migration. |
| [`priorite-suivi.html`](priorite-suivi.html) | La même spécification en page annotée, avec les maquettes d'IHM et une bascule de tri interactive. Page autonome, à ouvrir directement dans un navigateur. |

## Deux points restent à trancher

1. **Le rouge est déjà pris par l'ALD** (libellé rouge `#C00000`). Les deux signaux cohabitent parce qu'ils n'occupent ni la même zone, ni la même forme, ni la même teinte — mais un coût résiduel subsiste. L'issue radicale, si ça gêne à l'usage : retirer le rouge du libellé ALD, qui est un statut administratif là où l'importance est un jugement clinique. Voir §2.
2. **Recouvrement avec la case « À suivre »**, qui dit presque la même chose. Voir §7.

## À l'attention de l'implémentation

Le **compte de carrés 3 / 2 / 1 n'est pas décoratif**. Rouge, orange et vert forment exactement l'axe qu'une deutéranopie ne distingue pas (~8 % des hommes), et c'est aussi la seule information qui survit à l'impression noir et blanc du module. Trois carrés pleins de couleurs différentes feraient perdre les deux garde-fous d'un coup.

---

Les épisodes qui servent d'exemples dans la spécification et les maquettes sont **fictifs**.
