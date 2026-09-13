# Le labo de poche

Jeu mobile (iPhone / iPad) pour apprendre les noms du matériel de TP de
sciences de 6<sup>e</sup>, d'après la fiche méthode « Le matériel de TP
(REA — je sais identifier le matériel utilisé dans les laboratoires) ».

Sans rapport avec la proposition d'ergonomie XMED qui occupe la racine du
dépôt : dossier autonome, aucun fichier partagé, la maquette
`../index.html` n'est pas touchée.

## Contenu

Un seul fichier, `index.html`, sans dépendance hormis deux familles
Google Fonts. Les 21 objets sont redessinés en SVG inline — pas de photos,
donc rien à charger et un rendu identique en thème clair et sombre.

## Les deux niveaux

| Niveau | Déroulé |
|--------|---------|
| **Je choisis** | Le nom est à trouver parmi trois propositions, tirées dans la même série pour que la confusion soit plausible. |
| **Je dis à voix haute** | Aucune proposition. L'enfant nomme l'objet, appuie sur *Vérifier*, puis s'auto-évalue. Se débloque une fois le premier niveau terminé. |

Les 21 objets sont répartis en trois séries de sept (verrerie de base,
mesurer et prélever, observer et chauffer), plus une révision générale de
douze objets tirés au hasard, ouverte une fois les trois séries faites.
Le nom est lu par la synthèse vocale du téléphone à chaque correction ;
le haut-parleur de la barre coupe le son. Les ratés d'une manche sont
rejouables immédiatement depuis le bilan.

## Ce qui est conservé

Les étoiles et le réglage du son vivent dans le `localStorage` de
l'appareil : chaque tablette garde sa propre progression, rien ne part sur
un serveur. « Effacer les étoiles », en bas de l'accueil, remet à zéro.
