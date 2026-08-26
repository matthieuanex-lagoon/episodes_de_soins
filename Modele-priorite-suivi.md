# Modèle — Importance du suivi des épisodes de soins

Spécification fonctionnelle.
Vue détaillée = fenêtre « Episodes et suivis en cours ». Cadre compact = widget de la feuille globale.
Maquette d'intention : `index.html` → https://matthieuanex-lagoon.github.io/episodes_de_soins/

> **Objectif, en une phrase : voir d'emblée ce qui doit être priorisé et important.**

Vocabulaire et encodage arrêtés avec Sophie : libellé **Importance** (et non « Priorité »), valeurs **haute / moyenne / basse** (aucun chiffre affiché), encodage par **petits carrés** — nombre + couleur.

## 1. Le problème : tout est au même niveau

Le cadre n'est pas mal trié, il est **trié sur des critères qui ne portent aucune information clinique**. L'ordre alphabétique classe sur la première lettre d'un libellé ; l'ordre chronologique, sur le moment où quelqu'un a ouvert une ligne. Aucun des deux ne répond à la question de début de consultation.

Sur le dossier d'exemple (§3) :

- **Sciatique** et **nodule pulmonaire sans précision** ont été ouverts le même jour. Voisins en tri chronologique, voisins en tri alphabétique, deux lignes noires identiques. L'une se résoudra seule, l'autre est une incertitude à lever.
- L'**artériopathie oblitérante**, revascularisée l'an dernier et sous surveillance échographique semestrielle, tombe en huitième position au tri chronologique — parce qu'elle a été ouverte en 2002.
- L'**insuffisance mitrale** n'a plus été touchée depuis 2011. Rien ne le signale.

Le rouge existant n'y remédie pas : il signale une **ALD**, c'est-à-dire une prise en charge administrative, sans rapport avec ce qui doit être revu aujourd'hui. Le nodule pulmonaire n'est pas en ALD.

## 2. Ce que le niveau mesure

Le niveau exprime l'**importance du suivi** (charge de surveillance actuelle), pas la gravité intrinsèque de la pathologie, ni l'ancienneté du problème. Il est donc **mutable dans le temps** et doit être ré-évaluable en une touche.

> **Dire « importance du suivi » en toutes lettres** partout où la place le permet — panneau, infobulle, en-tête d'impression, menu contextuel. « Importance » seul se lit comme l'importance de la maladie, lecture que cette section écarte.

### L'incertitude compte autant que la gravité

Point le plus important de la spécification. **Un nodule pulmonaire sans précision n'est pas un diagnostic grave : c'est un diagnostic absent.** Rien n'est établi, l'enjeu potentiel est majeur, le calendrier de contrôle est court. Il mérite le niveau le plus haut non pas malgré son imprécision, mais *à cause d'elle*.

Le niveau haut se justifie donc par deux voies distinctes :

1. **Gravité établie sous surveillance active** — artériopathie revascularisée : on sait ce que c'est et ce que ça exige.
2. **Gravité possible non écartée** — nodule pulmonaire, lésion pancréatique en attente de contrôle. Ce qu'on ne sait pas encore est ce qui doit remonter le plus vite.

C'est la seconde voie que le tri actuel dessert le plus : un épisode ouvert hier, sans code, sans note, sans ALD, ne se distingue par rien.

### Les niveaux

| Rendu | Niveau | Définition opérationnelle |
|-------|--------|---------------------------|
| 3 carrés rouges | Haute | Action ou contrôle attendu à échéance courte (< 3 mois). Pathologie instable, en traitement d'attaque, sous surveillance rapprochée — **ou incertitude portant sur un enjeu grave, non levée**. |
| 2 carrés orange | Moyenne | Chronique stabilisé, contrôle périodique planifié (3–12 mois). Rien à décider aujourd'hui, mais l'épisode pilote des contrôles récurrents et son abandon se paierait. |
| 1 carré vert | Basse | Aucune surveillance programmée, mais l'épisode reste pertinent (contexte, antécédent, contre-indication, traçabilité). |
| colonne vide | Non définie | Pas encore trié. État par défaut à la création et pour tout l'historique. Rangé en fin de tri, jamais mêlé aux niveaux bas. |

- Les carrés non atteints restent affichés **en gris clair** : c'est ce qui rend l'échelle explicite.
- Sur la ligne **non définie**, la colonne est **entièrement vide**, pas même les carrés gris.
- **Aucun chiffre n'apparaît dans l'interface.** Le champ reste numérique en base (tri), sans jamais remonter à l'IHM.

## 3. Dossier d'exemple, épisode par épisode

Onze épisodes, deux ALD, vingt-cinq ans d'historique. Les niveaux marqués *(proposé)* sont soumis à validation.

| Niveau | Épisode | Pourquoi ce niveau |
|--------|---------|--------------------|
| Haute | **Artériopathie oblitérante des membres inférieurs** — ALD, I73.9, depuis 2002 | Gravité établie sous surveillance active : revascularisation l'an dernier, contrôle échographique semestriel programmé. Le niveau haut « classique ». |
| Haute | **Nodule pulmonaire, sans précision** — ouvert le 26/08/2026 | Gravité possible non écartée. Ni code, ni note, ni ALD, et pourtant l'épisode qui doit remonter le plus vite. **C'est l'incertitude qui fixe le niveau.** |
| Haute *(proposé)* | **TIPMP du pancréas** — depuis 2024 | Lésion à potentiel de dégénérescence, contrôle écho-endoscopique noté « à faire ». Un contrôle en attente qui traîne est ce qu'un niveau haut doit rendre visible. |
| Moyenne *(proposé)* | **Surveillance coloscopique** — Z12.1, depuis 2010 | Surveillance programmée à échéance longue, dernière coloscopie sans anomalie. L'épisode existe pour ne pas laisser passer l'échéance suivante. |
| Moyenne | **Flutter et fibrillation auriculaire** — I48, depuis 2026 | Trouble du rythme récent mais cadence de suivi posée. Passerait en haut si le traitement était en cours d'ajustement. |
| Moyenne *(proposé)* | **Tabagisme** — Z72.0, sevré depuis 2022 | Facteur de risque commun de l'artériopathie *et* du nodule : il conditionne les deux suivis les plus hauts. Le sevrage se surveille. Le niveau bas se défendrait si on le tenait pour acquis. |
| Moyenne | **Hypercholestérolémie** — ALD, E78.0, depuis 2002 | Chronique traitée, bilan annuel. Dernier contact il y a trois ans : échéance non tenue, cf. §10. |
| Moyenne | **Hypothyroïdie** — E03.9, depuis 2013 | Fruste, anticorps positifs. Contrôle biologique périodique, sans décision en attente. |
| Moyenne | **Insuffisance mitrale (non rhumatismale)** — I34.0, depuis 2009 | Valvulopathie relevant d'une échographie périodique. Dernier contact 2011, quinze ans. Le niveau ne corrige pas l'oubli, il le rend visible. |
| Basse | **Sciatique** — M54.3, ouvert le 26/08/2026 | Épisode aigu, résolution attendue, aucune surveillance programmée. Ouvert le même jour que le nodule pulmonaire : deux lignes aujourd'hui identiques, désormais séparées par trois crans. |
| Non définie | **Non-Classé** — depuis 2001 | Épisode fourre-tout jamais qualifié : le classer serait lui prêter une intention qu'il n'a pas. |

**Distribution attendue** : trois hauts, six moyens, un bas, un non défini. Si tout finit en haut, le dispositif ne trie plus rien — **un dossier chargé doit produire deux ou trois hauts, pas huit**. Règle d'usage à porter en formation, pas contrainte technique.

Le niveau **ne remplace ni le code CIM10, ni l'ALD, ni la note libre**. Il ne dit pas ce qu'est l'épisode : il dit quelle place lui donner dans une consultation de quinze minutes.

## 4. Le rouge, déjà occupé par l'ALD — point à trancher

Deux libellés rouges dans ce dossier (artériopathie, hypercholestérolémie). Le feu tricolore réclame une couleur prise. Tenable à trois conditions :

1. **Zones disjointes** — carrés dans une gouttière de 32 px à l'extrême gauche, rouge ALD sur le libellé.
2. **Formes disjointes** — trois petits carrés contre du texte.
3. **Teintes séparées** — vermillon `#D33A2C` pour l'importance, rouge sombre `#C00000` pour l'ALD.

Le dossier fournit l'argument décisif pour ne pas fusionner les deux signaux : l'artériopathie est **rouge et haute**, l'hypercholestérolémie **rouge et moyenne**, le nodule pulmonaire **noir et haut**. Les trois combinaisons coexistent dans le même écran.

**Issue radicale si le coût gêne à l'usage** : retirer la coloration rouge du libellé ALD, l'information restant portée par la colonne `ALD` et ses dates. L'ALD est un **statut administratif**, l'importance du suivi un **jugement clinique** ; si un seul mérite le rouge, ce n'est pas l'ALD. À ne décider qu'après usage réel.

**Daltonisme — contrainte non négociable.** Rouge / orange / vert est exactement l'axe qu'une deutéranopie ne distingue pas (~8 % des hommes). Le compte de carrés 3/2/1 n'est pas un confort : c'est la seule lecture fiable pour ces utilisateurs, et la seule qui survive à l'impression N&B.

## 5. Codage visuel

Colonne dédiée de **32 px à l'extrême gauche**, avant `Acteur`, ne contenant que trois carrés de 7 px espacés de 2 px.

| Niveau | Couleur | Carrés pleins |
|--------|---------|---------------|
| Haute | `#D33A2C` | 3 / 3 |
| Moyenne | `#DB7500` | 2 / 3 |
| Basse | `#2E8B45` | 1 / 3 |
| Non définie | — | 0, colonne vide |

Emplacements non atteints : `#DCDCDC`.

- Colonne **dessinée en propriétaire**, **fond gris conservé même sur ligne sélectionnée** : elle se comporte en gouttière, le contraste des carrés ne bouge jamais.
- **Triable au clic**, contrairement à la colonne d'indicateur du système — c'est ce qui permet de se passer de colonne texte.
- **En-tête de colonne** : 32 px ne tiennent pas le mot « Importance », et une abréviation n'apprend rien. L'en-tête affiche **les trois carrés en gris** — légende permanente de l'encodage et cible de tri, la flèche s'y installant normalement. Le nom complet vit dans l'infobulle d'en-tête, le sélecteur de colonnes, le bandeau de regroupement, l'en-tête d'impression et le menu contextuel.
- Le libellé **reste noir**, sauf ALD.
- Infobulle de ligne : `Importance du suivi : haute — contrôle attendu sous 3 mois · définie le 26/08/2026 par MAN`.
- **Cadre compact** : gouttière et carrés identiques. Il ne montre que sept lignes sur onze, d'où le tri par importance par défaut (§7).
- **Impression N&B** : trois gris voisins ; le compte de carrés porte seul l'information.

## 6. La saisie

### Le risque n'est pas l'ergonomie, c'est le démarrage à froid

Si tout part à `NULL`, le premier jour le cadre affiche exactement ce qu'il affiche aujourd'hui : rien. La valeur n'arrive qu'après que chaque dossier a été classé à la main, sans contrepartie immédiate. Un praticien qui ouvre trois dossiers de onze épisodes et doit les trier avant d'y gagner quoi que ce soit abandonne au quatrième. **Le coût est payé d'avance, le bénéfice arrive après : le profil d'adoption le plus défavorable qui soit.** Le reste de cette section est du réglage ; ceci est structurel.

### Une proposition à valider, pas une colonne vide

À la première ouverture d'un dossier, chaque épisode reçoit un niveau **proposé**, et sa cellule de gouttière porte un **fond hachuré** signifiant « personne n'a encore regardé ». Un clic n'importe où dans la cellule valide tel quel ; un clic dans l'une des trois zones pose un autre niveau et valide dans le même geste. Le premier passage devient une *relecture* — deux ou trois corrections sur onze lignes — au lieu de onze décisions à composer.

Règles de proposition, sans prétention clinique : elles ne décident pas, elles mettent en page un point de départ.

| Si l'épisode… | Proposition |
|---------------|-------------|
| a été ouvert dans les trois derniers mois | **Haute** — quelque chose est en cours |
| porte une ALD active, ou la case « À suivre » | **Moyenne** — un suivi existe |
| a une date de fin, ou plus de contact depuis 5 ans sans ALD | **Basse** — plus rien n'est programmé |
| aucun de ces cas | **Moyenne** — le milieu, le moins faux par défaut |

### Pourquoi ce n'est pas l'attribution automatique écartée

Ce point revient sur une décision antérieure, et il faut le dire franchement. Le choix « manuel uniquement » était juste sur la question qu'il tranchait : aucune machine ne doit décider de l'importance d'un suivi, et un niveau déduit du CIM10 serait faux une fois sur deux — le nodule pulmonaire n'a ni code, ni note, ni ALD, et c'est l'un des trois épisodes les plus importants.

Mais ce qui était refusé, c'est **l'autorité** de la machine, pas son aide. Un niveau proposé et visiblement non validé n'a aucune autorité : il ne survit pas au premier regard, et le hachuré dit à qui regarde l'écran que personne ne l'a endossé. Toute la différence tient dans le fait que l'état « non validé » **se voie**. Retirez le hachuré, on retombe exactement sur ce qui avait été écarté.

### Poser un niveau : trois gestes

1. **La gouttière**, cliquable en trois zones (§10). Le geste principal.
2. **Menu contextuel** : clic droit sur une ou plusieurs lignes → « Importance du suivi ▸ ». La multi-sélection reste requise pour traiter plusieurs lignes d'un coup.
3. **Panneau de détail** : contrôle segmenté `Aucune | Haute | Moyenne | Basse` sous la case « À suivre ». Seul endroit où saisir un motif.

Et le clavier : touches `1` `2` `3` de la plus haute à la plus basse, `0` ou `Suppr` retire le niveau. Pas de confirmation, annulable par Ctrl+Z. Les chiffres survivent ici parce qu'une rangée de touches est ordonnée par nature — rien n'est affiché.

### Classer au moment où l'on y pense

Personne ne s'assoit pour trier des épisodes. On touche un épisode quand on consulte à son sujet — le seul moment où le jugement est disponible sans effort. Le contrôle doit être présent à cet instant, dans le panneau ouvert pendant la consultation, et **pré-sélectionné tant que le niveau n'est pas validé**. Une fonctionnalité qui exige une séance de rangement séparée n'aura jamais lieu.

**Corollaire sur la fraîcheur** : un niveau haut sans contact depuis six mois est soit un niveau à baisser, soit un suivi qui a décroché. Dans les deux cas cela doit se voir, et le signal porte sur la cellule `Dernier contact`, jamais sur les carrés — un glyphe, un sens. **Un niveau qui ment est pire qu'une colonne vide**, ce qui range la péremption du côté du cœur et non des suites (§11).

### Un miroir, pas un garde-fou

En pied de la vue détaillée, un discret « *11 validées sur 11 · dont 3 hautes* ». Aucune limite, aucun avertissement, aucun blocage — juste le reflet. C'est ce qui empêche la dérive où tout finit en haut et où le tri ne dit plus rien, et cela ne coûte qu'une ligne de barre d'état.

## 7. Tri

Clé de tri : `ISNULL(IMPORTANCE, 9) ASC, DERNIER_CONTACT DESC`.

Le tri secondaire n'est pas cosmétique : dans le bloc moyen du dossier d'exemple, il fait remonter la surveillance coloscopique vue ce jour et descendre l'insuffisance mitrale abandonnée depuis 2011. **L'ordre à l'intérieur d'un niveau raconte l'entretien du dossier.**

| Vue | Tri par défaut | Justification |
|-----|----------------|---------------|
| Cadre compact | Importance, puis dernier contact décroissant | Balayé en deux secondes, et sept lignes visibles sur onze : ce qu'il coupe doit être ce qui compte le moins. |
| Vue détaillée | Dernier tri choisi, mémorisé par praticien. Premier lancement : importance. | Vue de gestion : le tri alphabétique ou par date y reste légitime. |

- Premier clic sur la gouttière : les rouges en haut. Ordre inverse au second clic.
- **Ne jamais re-trier pendant l'édition** : la ligne ne bouge pas sous le curseur ; le nouvel ordre s'applique au rafraîchissement. Sinon le classement en série — ce qu'on fait à la première ouverture d'un dossier de onze épisodes — devient impraticable.
- **Groupement** à la demande via le bandeau existant + raccourci au menu contextuel. Pas par défaut : trois en-têtes de groupe coûtent trois lignes sur sept visibles.

## 8. Modèle de données

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

Teintes et nombre de carrés en base plutôt qu'en dur dans l'IHM : la teinte du rouge se règle sans livrer une version, ce qui rend l'arbitrage du §4 réversible à peu de frais.

**La proposition (§6) ne se stocke pas.** Elle se calcule à l'affichage, et `IMPORTANCE_MAJ` suffit à distinguer les trois états sans colonne supplémentaire :

| État | Test | Rendu |
|------|------|-------|
| Personne n'a regardé | `IMPORTANCE_MAJ IS NULL` | proposition, cellule hachurée |
| Jugement posé | `MAJ` renseignée, `IMPORTANCE` renseignée | carrés pleins |
| Niveau délibérément retiré | `MAJ` renseignée, `IMPORTANCE IS NULL` | colonne vide |

Aucune migration n'est donc nécessaire : tout l'historique existant se présente d'emblée comme proposé, ce qui est exactement l'état de fait.

**Historisation** : tracer les changements dans le journal d'événements du dossier (ancien → nouveau, date, acteur). Un nodule pulmonaire classé haut puis redescendu après un contrôle rassurant est une décision de suivi qui doit laisser une trace datée.

**Clôture** : `Clore épisode` ne remet pas `IMPORTANCE` à NULL ; l'épisode sort de la vue « en cours » par le jeu de `Date fin`.

## 9. Point à trancher — recouvrement avec « À suivre »

Le dossier d'exemple montre l'incohérence déjà à l'œuvre : `À suivre` est cochée sur l'artériopathie, l'hypercholestérolémie et l'insuffisance mitrale — **mais pas sur le nodule pulmonaire ni sur la TIPMP**, qui sont pourtant ce qu'il y a de plus à suivre.

1. **Garder la case en lecture seule**, cochée automatiquement dès qu'une importance haute ou moyenne est posée. Saisie unique, compatibilité préservée. *Préférence.*
2. **Retirer `À suivre`** après migration : `À suivre` ≡ `IMPORTANCE IN (1,2)`. Plus propre, impacte filtres et exports.
3. Les garder indépendantes — à écarter : l'état actuel du dossier est exactement ce que produit cette option.

## 10. Deux pistes étudiées pour la saisie

**Constat de terrain d'abord** : le tri par la case `À suivre` est déjà en place dans le dossier. Quatre épisodes cochés remontent en tête — insuffisance mitrale, hypercholestérolémie, nodule pulmonaire, artériopathie — dans cet ordre, soit l'insuffisance mitrale abandonnée depuis 2011 devant le nodule ouvert ce matin. Un drapeau binaire crée un bloc de tête sans hiérarchie interne, et le bloc grossit jusqu'à ne plus rien dire. C'est la démonstration la plus courte du besoin de trois niveaux, et elle vient de l'usage.

### Piste A — trois feux à la place de « À suivre », qui se renforcent au clic

La colonne `À suivre` est remplacée par trois pastilles pâles (verte, orange, rouge) ; un clic sature l'une d'elles. La cellule est à la fois l'affichage et la commande.

**Apports** — dissout l'arbitrage du §9 : le champ n'est pas doublé, il est remplacé par celui qui tenait déjà son rôle. Un clic par épisode sans quitter la grille, ni sélection, ni menu, ni panneau : la saisie la plus rapide possible pour classer un dossier au premier passage. Aucune largeur nouvelle, la colonne existe déjà.

**Coûts sous la forme littérale** — le signal s'affaiblit : pâle contre saturé est un écart bien plus faible que « trois marques contre une », et toutes les lignes portent la même masse colorée ; il faut comparer des intensités au lieu de compter. La redondance non colorée se dégrade (il reste la position de la pastille saturée, moins franche à l'impression et pour une deutéranopie). Trois cibles de 9 px dans une ligne de 24 px, sur une cellule qui sert aussi à sélectionner la ligne : le clic accidentel pose un niveau. Retirer un niveau demande un geste caché.

**Forme retenue — la gouttière cliquable.** Garder la gouttière déjà spécifiée (comptage 3/2/1, hors du bandeau de sélection) et la rendre cliquable en trois zones de 10 px sur toute la hauteur de la ligne, le survol montrant ce que le clic poserait. Un seul objet, optimisé pour lire à gauche et pour écrire au clic. `À suivre` est retiré.

### Piste B — un rang par épisode, monté ou descendu à la flèche

**Apports** — expressivité totale, aucun palier imposé, aucune égalité. Départage à l'intérieur d'un niveau, là où le tri actuel se rabat sur le dernier contact. Le geste ne s'apprend pas.

**Coûts** :

- **Le coût est celui du dossier, pas de l'épisode.** Poser un niveau est une décision isolée ; poser un rang oblige à se situer face à tous les autres, à chaque nouvel épisode. La sciatique du jour arrive en rang 11 sur 11 : dix actionnements de flèche.
- **Un rang ne signifie rien hors de son dossier.** Ni filtrable, ni colorable, ni agrégeable au cabinet, et aucune règle de péremption possible. Toutes les suites du §11 disparaissent.
- **Il n'y a rien à afficher.** Le rang *est* la position de la ligne : dès qu'on trie autrement, l'information s'évanouit. Inverse exact de la propriété défendue au §5 — un signal porté par la ligne, pas par sa place.
- **Pas de fusion à deux praticiens.** Un ordre total : le second qui reclasse écrase le jugement du premier.
- **Dégradation brutale.** Un niveau ancien reste à peu près juste ; un ordre non entretenu est simplement faux.

### Recommandation

**Piste A dans sa forme « gouttière cliquable ». Pas la piste B.**

Si le besoin exprimé par la piste B est « celui-là d'abord, aujourd'hui », la réponse économique est **une épingle** : un épisode remonté en tête indépendamment de son niveau, à un seul état, sans ordre total à maintenir ni conflit entre praticiens. À verser aux suites, pas à la version 1.

## 11. Reprise de l'existant, et la suite

**Il n'y a pas de reprise**, et c'est l'intérêt du dispositif du §6 : l'historique se présente d'emblée comme proposé, dossier par dossier, au moment où on l'ouvre. Pas de bandeau « N épisodes non classés » à écarter, pas de campagne de rattrapage, pas de fenêtre modale — le hachuré dit la même chose, ligne par ligne, là où l'action a lieu.

### Péremption du niveau — désormais réclamée au cœur

Le §6 argumente que cette règle n'est pas une suite mais une condition : un niveau qui ment est pire qu'une colonne vide. Ce qui reste ici, c'est son réglage fin — quel délai par niveau, et jusqu'où pousser le signalement.

Le dossier contient deux niveaux moyens dont l'échéance n'est plus tenue : hypercholestérolémie sous ALD vue il y a trois ans, insuffisance mitrale vue il y a quinze ans. Un niveau moyen **affirme** qu'un contrôle périodique existe ; quand le dernier contact dépasse largement la période annoncée, le niveau ment.

Un signalement discret sur ces lignes — quatrième carré vide cerclé, teinte d'infobulle — ferait passer le dispositif de « ce qui compte » à « ce qui compte et a décroché ». Hors périmètre initial, mais c'est là que se trouve la valeur du champ à deux ans.

### Autres suites

- **L'épingle** — remonter un épisode en tête du dossier indépendamment de son niveau, pour la consultation du jour. La part utile de la piste B (§10), à un seul état.
- Filtre rapide *importance haute seulement* dans le cadre compact.
- Restitution du niveau dans les exports et le volet d'impression.
- Report du niveau sur le regroupement par acteur, en cabinet de groupe.

---

*Le dossier d'exemple est dérivé d'un cas réel : libellés, codes et niveaux conservés, jours et mois des dates de début décalés, notes libres généralisées.*
