# Importance du suivi — proposition d'ergonomie

Module « Episodes et suivis en cours ». Maquette : `index.html` → https://matthieuanex-lagoon.github.io/episodes_de_soins/

> **Objectif : voir d'emblée ce qui doit être priorisé et important.**

Ce document ne traite ni du modèle de données ni de la reprise de l'existant. Il présente les représentations étudiées, ce que chacune donne à l'écran, et celle qui est retenue.

## Principes actés

- **Rien n'est attribué par la machine.** À la création d'un épisode, la colonne est vide et le reste jusqu'à décision du praticien. Aucune déduction depuis le CIM10, l'ALD ou la case « À suivre », et aucune proposition pré-remplie même si elle paraît logique sur le moment.
- **Le logiciel n'utilise pas le clic droit.** Aucune solution ne peut reposer sur un menu contextuel.
- **Vocabulaire arrêté avec Sophie** : « Importance », valeurs haute / moyenne / basse, aucun chiffre affiché.

## 1. Le problème

Le cadre n'est pas mal trié : il est trié sur des critères qui ne portent aucune information clinique. L'ordre alphabétique classe sur la première lettre d'un libellé, l'ordre chronologique sur le moment où quelqu'un a ouvert une ligne.

Sciatique et nodule pulmonaire, ouverts le même jour, occupent deux lignes rigoureusement identiques. L'une se résoudra seule, l'autre est une incertitude à lever.

Le tri par la case `À suivre` est le contournement que l'usage a déjà produit, et il montre ce qui manque : un drapeau binaire crée un bloc de tête sans hiérarchie interne — l'insuffisance mitrale abandonnée depuis 2011 s'y retrouve devant le nodule ouvert ce matin — et le bloc grossit jusqu'à ne plus rien dire.

## 2. Quatre représentations étudiées

Toutes reposent sur la même échelle : **trois marques pour ce qui compte le plus, deux pour un suivi programmé, une pour une simple veille.** Elles diffèrent par la forme et par ce qu'elles coûtent au regard.

| Piste | Forme | Verdict |
|-------|-------|---------|
| **1. Barre verticale segmentée** | Filet de 5 px sur toute la hauteur de la ligne, segmenté en trois, dans une gouttière à gauche. | *Écartée.* Les segments se touchent : à 24 px de hauteur de ligne, deux contre trois se distinguent mal, et un filet plein se lit comme une bordure décorative plutôt que comme une donnée. |
| **2. Trois petits carrés** | Trois carrés de 7 px séparés de 2 px, même gouttière. Emplacements non atteints en gris clair. | **Retenue.** On compte au lieu de mesurer. L'échelle est explicite : un carré vert suivi de deux vides dit « un sur trois ». |
| **3. Feu tricolore remplaçant « À suivre »** | Trois pastilles pâles dans la colonne existante ; celle du niveau se sature au clic. | *Écartée.* Son mérite réel est de supprimer le recouvrement avec « À suivre ». Mais elle pose trois marques colorées sur *chaque* ligne : la distinction ne tient plus à une quantité mais à une saturation, écart bien plus faible au milieu d'une masse chromatique uniforme. |
| **4. Rang manuel** | Un rang par épisode, monté ou descendu à la flèche, tri sur le rang. | *Écartée.* Le coût est celui du dossier et non de l'épisode. Un rang ne signifie rien hors de son dossier, ne s'affiche nulle part ailleurs que dans sa propre position, et deux praticiens qui reclassent s'écrasent l'un l'autre. |

## 3. La proposition retenue

Trois carrés dans une **gouttière de 32 px** à l'extrême gauche, avant `Acteur`. Cellule dessinée en propriétaire, **fond gris conservé même sur ligne sélectionnée** — le contraste des carrés ne bouge jamais — mais **triable au clic**, ce qui permet de se passer de colonne texte.

| Niveau | Ce qu'il désigne |
|--------|------------------|
| **Haute** — 3 carrés rouges | Contrôle attendu sous trois mois. Pathologie instable, en traitement d'attaque — ou **incertitude portant sur un enjeu grave**, non levée. Un nodule pulmonaire sans précision n'est pas un diagnostic grave : c'est un diagnostic absent, et c'est ce qui le met en haut. |
| **Moyenne** — 2 carrés orange | Chronique stabilisé, contrôle périodique de trois à douze mois. Rien à décider aujourd'hui, mais l'épisode pilote des contrôles récurrents. |
| **Basse** — 1 carré vert | Aucune surveillance programmée, mais l'épisode reste pertinent : contexte, antécédent, contre-indication, traçabilité. |
| **Vide** — aucun carré | Aucun niveau posé. État par défaut à la création et pour tout l'historique. Rangé en fin de tri, jamais mêlé aux niveaux bas. |

Couleurs : `#D33A2C`, `#DB7500`, `#2E8B45`, emplacements non atteints `#DCDCDC`.

**Deux règles de rendu non négociables :**

1. **Le compte de carrés porte l'information sans la couleur.** Rouge / orange / vert est exactement l'axe qu'une deutéranopie ne distingue pas (~8 % des hommes), et l'impression du module est en noir et blanc. Le comptage 3/2/1 est la seule lecture qui survit aux deux.
2. **Le libellé reste noir, sauf ALD.** Le rouge du texte appartient déjà à l'ALD ; le lui disputer ferait perdre les deux signaux.

**En-tête de colonne** : 32 px ne tiennent pas le mot « Importance » et une abréviation n'apprend rien — l'en-tête affiche les trois carrés en gris, légende permanente et cible de tri. Le nom complet vit dans l'infobulle, le sélecteur de colonnes et l'en-tête d'impression.

## 4. La saisie

Sans clic droit, trois gestes seulement :

| Geste | Où, et pour quoi |
|-------|------------------|
| **Clic dans la gouttière** | Le geste principal, dans la grille. Trois zones de 10 px sur toute la hauteur de la ligne, une par niveau ; le survol montre ce que le clic poserait. Recliquer le niveau actif l'efface. |
| **Touches `1` `2` `3` `0`** | Sur la ligne sélectionnée, et sur **toutes les lignes sélectionnées** — ce qui remplace le menu contextuel pour traiter un dossier entier. Annulable par `Ctrl+Z`, sans confirmation. |
| **Panneau de détail** | Contrôle segmenté `Aucune \| Haute \| Moyenne \| Basse` sous la case « À suivre ». « Aucune » est en première position : c'est l'état de départ de tout épisode, il doit rester atteignable d'un clic. |

**Un miroir, pas un garde-fou** : en pied de la vue détaillée, un discret « *10 niveaux posés sur 11 · dont 3 hautes* ». Aucune limite, aucun avertissement — juste le reflet, pour éviter la dérive où tout finit en haut.

## 5. Le tri

Par importance décroissante, puis par dernier contact décroissant. Les épisodes sans niveau se rangent en fin de liste, jamais mêlés aux niveaux bas.

| Vue | Tri par défaut |
|-----|----------------|
| Cadre compact, feuille globale | Importance. Balayé en deux secondes, sept lignes visibles sur onze : ce qu'il coupe doit être ce qui compte le moins. |
| Vue détaillée | Dernier tri choisi, mémorisé par praticien, importance au premier lancement. |

- **Ne jamais re-trier pendant l'édition.** Poser un niveau ne déplace pas la ligne sous le curseur ; le nouvel ordre s'applique au rafraîchissement ou sur le bouton qui apparaît. Sinon le classement en série devient impraticable.
- **Le tri secondaire n'est pas cosmétique.** À l'intérieur d'un niveau, l'ordre par dernier contact fait remonter ce qui est entretenu et descendre ce qui a décroché.

## 6. Ce qui reste à trancher

| Sujet | État |
|-------|------|
| Le rouge du libellé, porté par l'ALD | **Ouvert.** Les deux rouges cohabitent parce qu'ils n'occupent ni la même zone, ni la même forme, ni la même teinte — et le dossier prouve qu'ils ne sont pas substituables : une ligne rouge et haute, une rouge et moyenne, une noire et haute. Reste l'option de retirer le rouge du libellé ALD, statut administratif là où l'importance est un jugement clinique. |
| Recouvrement avec « À suivre » | **Ouvert.** Un épisode haut ou moyen est par définition à suivre, et la case est déjà incohérente : cochée sur l'insuffisance mitrale, pas sur le nodule. Soit on la garde en lecture seule, soit on la retire. |
| Vieillissement des niveaux | **À étudier.** Un niveau haut sans contact depuis six mois est soit un niveau à baisser, soit un suivi qui a décroché. Si ce signal est ajouté, il portera sur la cellule `Dernier contact` et non sur les carrés — un glyphe, un sens. |
| Nommage | **Arrêté** avec Sophie. |

---

*Le dossier d'exemple est dérivé d'un cas réel : libellés, codes CIM10 et niveaux conservés, jours et mois des dates de début décalés, notes libres généralisées.*
