# Modèle — Importance du suivi des épisodes de soins

Spécification fonctionnelle.
Vue détaillée = fenêtre « Episodes et suivis en cours ». Cadre compact = widget de la feuille globale.
Page de rendu : `priorite-suivi.html`.

Vocabulaire et encodage arrêtés avec Sophie : libellé **Importance** (et non « Priorité »), valeurs **haute / moyenne / basse** (aucun chiffre affiché), encodage par **petits carrés** — nombre + couleur.

## 1. Sémantique retenue

Le niveau exprime l'**importance du suivi** (charge de surveillance *actuelle*), pas la gravité intrinsèque de la pathologie. Conséquence assumée : un épisode grave mais stabilisé redescend de niveau ; un épisode bénin en cours d'exploration monte. Le niveau est **mutable dans le temps** et doit être ré-évaluable en un clic.

> **Dire « importance du suivi » en toutes lettres** partout où la place le permet — panneau, infobulle, en-tête d'impression, menu contextuel. « Importance » seul se lit comme l'importance de la maladie, exactement la lecture que cette section écarte. Le complément fait le travail.

| Rendu | Niveau | Définition opérationnelle | Dossier d'exemple |
|-------|--------|---------------------------|-------------------|
| 3 carrés rouges | Haute | Action ou contrôle attendu à échéance courte (< 3 mois). Pathologie instable, en cours d'exploration, en traitement d'attaque, ou événement récent nécessitant un revoir. | Palpitations, bilan en cours |
| 2 carrés orange | Moyenne | Chronique stabilisé, contrôle périodique planifié (3–12 mois). Rien à décider aujourd'hui, mais l'épisode pilote des contrôles récurrents. | Diabète de type 2 non insulinodépendant (ALD) |
| 1 carré vert | Basse | Aucune surveillance programmée, mais l'épisode reste pertinent (contexte, contre-indication, facteur de risque, traçabilité). | Entorse de cheville, Certificat de sport |
| colonne vide | Non définie | Pas encore trié. État par défaut à la création et pour tout l'historique. | Non-Classé |

- Les carrés non atteints restent affichés **en gris clair** : c'est ce qui rend l'échelle explicite (un carré vert seul ne dit rien, un carré vert suivi de deux emplacements vides dit « un sur trois »).
- Sur la ligne **non définie**, la colonne est **entièrement vide**, pas même les carrés gris : un niveau bas et un niveau jamais examiné ne doivent pas se ressembler. Au tri, les non définies se rangent tout en bas, jamais mêlées aux basses.
- **Aucun chiffre n'apparaît dans l'interface.** Le champ reste numérique en base (nécessaire au tri), sans jamais remonter à l'IHM.

## 2. Le rouge, déjà occupé par l'ALD — point à trancher

Le libellé d'un épisode en ALD est rouge (`#C00000`). Le feu tricolore réclame donc une couleur prise. C'est tenable à trois conditions, tenues par la maquette :

1. **Zones disjointes** — les carrés vivent dans une gouttière de 32 px à l'extrême gauche, le rouge ALD sur le libellé au milieu de la ligne.
2. **Formes disjointes** — trois petits carrés contre du texte.
3. **Teintes séparées** — vermillon `#D33A2C` pour l'importance, rouge sombre `#C00000` pour l'ALD.

Coût résiduel à connaître : sur un dossier chargé, du rouge à gauche et du rouge au milieu se répondent visuellement même sans parler de la même chose.

**Issue radicale si le coût gêne à l'usage** : retirer la coloration rouge du libellé ALD, l'information restant portée par la colonne `ALD` et ses dates (une pastille y suffit). Argument de fond : l'ALD est un **statut administratif**, l'importance du suivi un **jugement clinique** ; si un seul mérite le rouge, ce n'est pas l'ALD. À ne décider qu'après usage réel.

**Daltonisme — contrainte non négociable.** Rouge / orange / vert est exactement l'axe qu'une deutéranopie ne distingue pas (~8 % des hommes). Le compte de carrés 3/2/1 n'est pas un confort : c'est la seule lecture fiable pour ces utilisateurs, et il ne peut pas sauter à l'implémentation.

## 3. Codage visuel

Colonne dédiée de **32 px à l'extrême gauche**, avant `Acteur`, ne contenant que trois carrés de 7 px espacés de 2 px.

| Niveau | Couleur | Carrés pleins |
|--------|---------|---------------|
| Haute | `#D33A2C` | 3 / 3 |
| Moyenne | `#DB7500` | 2 / 3 |
| Basse | `#2E8B45` | 1 / 3 |
| Non définie | — | 0, colonne vide |

Emplacements non atteints : `#DCDCDC`.

- La colonne est **dessinée en propriétaire** et **garde son fond gris même quand la ligne est sélectionnée** : elle se comporte en gouttière, le contraste des carrés ne bouge jamais.
- Contrairement à la colonne d'indicateur du système, elle est **triable au clic** — c'est ce qui permet de se passer de toute colonne texte.
- **En-tête de colonne** : 32 px ne tiennent pas le mot « Importance », et une abréviation n'apprend rien. L'en-tête affiche **les trois carrés en gris** — la légende de l'encodage reste ainsi visible en permanence et sert de cible de tri, la flèche de tri s'y installant normalement. Le nom complet vit dans l'infobulle de l'en-tête, le sélecteur de colonnes, le bandeau de regroupement, l'en-tête d'impression et le menu contextuel.
- Le libellé **reste noir**, sauf ALD. L'importance ne s'exprime jamais par la couleur du texte.
- Infobulle de ligne : `Importance du suivi : haute — contrôle attendu sous 3 mois · définie le 26/08/2026 par MAN`.
- **Cadre compact** : gouttière et carrés identiques, rien à réapprendre d'une vue à l'autre.
- **Impression N&B** : les trois teintes deviennent trois gris voisins ; le compte de carrés porte seul l'information — le même mécanisme que pour le daltonisme.

## 4. Attribution — 100 % manuelle

Aucune déduction depuis le CIM10/CISP, ni depuis ALD / À suivre / Facteur de risque. Le niveau est une décision clinique explicite, datée et signée (cabinet multi-acteurs, cf. colonne `Acteur`).

1. **Panneau de détail** : contrôle segmenté `Aucune | Haute | Moyenne | Basse` sous la case « À suivre », au-dessus de `Facteur de risque`. Seul endroit où saisir un motif.
2. **Menu contextuel de la grille** : clic droit sur une ou plusieurs lignes → « Importance du suivi ▸ ». La **multi-sélection est requise** : elle rend le rattrapage de l'historique supportable.
3. **Clavier** : ligne sélectionnée, touches `1` `2` `3` de la plus haute à la plus basse, `0` ou `Suppr` retire le niveau. Pas de confirmation, annulable par Ctrl+Z. Les chiffres survivent ici parce qu'une rangée de touches est ordonnée par nature — rien n'est affiché.

## 5. Modèle de données

```sql
ALTER TABLE EPISODE ADD IMPORTANCE        TINYINT      NULL;  -- 1 | 2 | 3 ; NULL = non définie
ALTER TABLE EPISODE ADD IMPORTANCE_MAJ    DATETIME     NULL;  -- date de la dernière décision
ALTER TABLE EPISODE ADD IMPORTANCE_ACTEUR VARCHAR(8)   NULL;  -- initiales praticien (cf. colonne Acteur)
ALTER TABLE EPISODE ADD IMPORTANCE_MOTIF  VARCHAR(120) NULL;  -- optionnel, panneau de détail seul

ALTER TABLE EPISODE ADD CONSTRAINT CK_EPISODE_IMPORTANCE
  CHECK (IMPORTANCE IS NULL OR IMPORTANCE IN (1,2,3));

CREATE TABLE REF_IMPORTANCE_SUIVI (
  CODE    TINYINT     NOT NULL PRIMARY KEY,  -- 1,2,3
  LIBELLE VARCHAR(40) NOT NULL,              -- 'Haute','Moyenne','Basse'
  COULEUR VARCHAR(7)  NOT NULL,              -- '#D33A2C','#DB7500','#2E8B45'
  CARRES  TINYINT     NOT NULL               -- 3,2,1
);
```

`1` = le niveau le plus haut. Convention de tri interne, jamais affichée : l'utilisateur ne voit que des carrés, le développeur ne manipule que des entiers.

Teintes et nombre de carrés en base plutôt qu'en dur dans l'IHM : la teinte du rouge se règle sans livrer une version, ce qui rend l'arbitrage du §2 réversible à peu de frais.

**Historisation** : tracer les changements de niveau dans le journal d'événements du dossier (ancien → nouveau, date, acteur). Ré-évaluer l'importance d'un suivi est une décision de suivi.

**Clôture** : `Clore épisode` ne remet pas `IMPORTANCE` à NULL ; l'épisode sort de la vue « en cours » par le jeu de `Date fin`.

## 6. Tri

Clé de tri : `ISNULL(IMPORTANCE, 9) ASC, DERNIER_CONTACT DESC`.

| Vue | Tri par défaut | Justification |
|-----|----------------|---------------|
| Cadre compact | Importance, puis dernier contact décroissant | Balayé en deux secondes en début de consultation ; il doit répondre à « qu'est-ce qui compte pour ce patient maintenant ». |
| Vue détaillée | Dernier tri choisi, mémorisé par praticien. Premier lancement : importance. | Vue de gestion : le tri alphabétique ou par date y reste légitime. |

- Premier clic sur la gouttière : les rouges en haut. Ordre inverse au second clic.
- **Ne jamais re-trier pendant l'édition** : la ligne ne bouge pas sous le curseur ; le nouvel ordre s'applique au rafraîchissement. Sinon le classement en série devient impraticable.
- **Groupement** à la demande via le bandeau existant + raccourci au menu contextuel. Pas par défaut : trois en-têtes de groupe coûtent trop de hauteur dans un cadre de cinq lignes.

## 7. Point à trancher — recouvrement avec « À suivre »

Un épisode d'importance haute ou moyenne est par définition « à suivre ». Indépendants, les deux champs produiront des dossiers incohérents.

1. **Garder la case en lecture seule**, cochée automatiquement dès qu'une importance haute ou moyenne est posée. Saisie unique, compatibilité préservée. *Préférence.*
2. **Retirer `À suivre`** après migration : `À suivre` ≡ `IMPORTANCE IN (1,2)`. Plus propre, impacte filtres et exports.
3. Les garder indépendantes — à écarter, faute d'une distinction énonçable en une phrase.

## 8. Reprise de l'existant

Aucune affectation automatique. Tous les épisodes existants passent à `NULL`.

Au premier accès d'un dossier après mise à jour, bandeau discret non bloquant en tête du cadre — « *N épisodes non classés* » — avec un lien ouvrant la vue détaillée en multi-sélection. Disparaît définitivement dès que le praticien l'écarte une fois, par dossier. Pas de fenêtre modale : elle serait fermée sans être lue, cinq fois par jour.

## 9. Extensions envisageables (hors périmètre initial)

- **Péremption du niveau** : un épisode d'importance haute dont le `Dernier contact` dépasse 3 mois mérite un signalement — tout l'intérêt d'un niveau haut est de rendre visible le suivi qui a décroché.
- Filtre rapide *importance haute seulement* dans le cadre compact.
- Restitution du niveau dans les exports et le volet d'impression.
