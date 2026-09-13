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
| **Je dis à voix haute** | Aucune proposition. L'enfant nomme l'objet, appuie sur *Vérifier*, puis s'auto-évalue. |
| **J'écris le nom** | Au clavier. Les fautes sont signalées et pointées (voir plus bas). La touche Entrée valide, pour ne pas avoir à viser un bouton derrière le clavier. |

Les deux derniers niveaux se débloquent une fois « Je choisis » terminé.

Les 21 objets sont répartis en trois séries de sept (verrerie de base,
mesurer et prélever, observer et chauffer), plus **Les 21 mélangés**, tout
dans le désordre, ouvert d'emblée et dans les deux niveaux.
Le nom est lu par la synthèse vocale du téléphone à chaque correction ;
le haut-parleur de la barre coupe le son. Les ratés d'une manche sont
rejouables immédiatement depuis le bilan.

## Ce que la saisie accepte

La comparaison ne corrige pas l'orthographe, elle reconnaît une intention,
en trois étages :

1. **Normalisation** — minuscules, accents retirés, traits d'union et
   apostrophes traités comme des espaces.
2. **Particules et pluriels** — `de`, `du`, `des`, `à`, `au`, `le`, `la`,
   `et`… sont ignorés, et le `s` final tombe. « Boîte de Pétri », « boite
   petri » et « boites de pétris » sont donc la même réponse.
3. **Fautes de frappe** — distance de Levenshtein : une faute jusqu'à huit
   lettres, deux au-delà. « Erlenmayer » et « cristalisoir » sont reconnus,
   mais **signalés**, pas avalés en silence.

Le garde-fou est au troisième étage : une saisie n'est acceptée que si elle
ressemble **plus** au nom attendu qu'à celui de n'importe quel autre des 21
objets. Sans cela, la tolérance de deux caractères validerait « pipette »
pour la pissette, et « verre » pour l'un ou l'autre des deux verres. Chaque
objet accepte aussi quelques raccourcis explicites (`petri`, `portoir`,
`brucelles`…), choisis pour ne valoir que pour lui.

Les deux premiers étages ne coûtent rien : écrire « boite petri » ou
« tubeaessai » est juste, sans remarque. Le troisième, lui, ne passe jamais
inaperçu : la réponse compte comme trouvée, mais l'écran affiche
**« Attention à l'orthographe »**, le nom correct, et la réponse de l'enfant
relue avec ses fautes pointées :

- une **lettre fausse ou en trop** est en rouge, soulignée d'une vague ;
- une **lettre oubliée** est marquée d'un point rouge à sa place — c'est la
  faute la plus fréquente, et la seule qu'on ne peut pas colorier autrement ;
- un accent manquant n'est jamais souligné : il ne compte pas.

Sur une consonne doublée, le point se place après la série (« enton·oir »),
pas avant : les deux positions coûtent autant à l'algorithme, une seule se
lit. Les objets mal orthographiés reviennent dans « À revoir » du bilan, au
même titre que les ratés.

Ces règles sont couvertes par une table de 76 cas, dans
`../outils/test-saisie.js`, à lancer par `node outils/test-saisie.js`.

## Dessins ou photos

Une bascule sur l'accueil change tous les visuels du jeu, y compris la fiche
et le bilan. Dix-neuf des vingt et un objets ont une photographie ; le verre
à pied et le porte-tubes n'avaient aucun candidat correct sur Wikimedia
Commons et gardent leur dessin, le repli étant automatique.

Les photos viennent toutes de **Wikimedia Commons**, sous licence libre
(CC BY-SA, CC0 ou domaine public), vérifiée fichier par fichier auprès de
l'API de Commons. Elles sont servies depuis `p/`, embarquées avec la page :
la politique de sécurité des artifacts interdit les images distantes, et cela
évite de dépendre d'un serveur tiers. L'écran « Crédits » nomme l'auteur et
la licence de chacune et renvoie au fichier d'origine, comme CC BY-SA
l'exige. Les dessins au trait, eux, ont été faits pour ce jeu.

## Ce qui est conservé

Les étoiles et le réglage du son vivent dans le `localStorage` de
l'appareil : chaque tablette garde sa propre progression, rien ne part sur
un serveur. « Effacer les étoiles », en bas de l'accueil, remet à zéro.
