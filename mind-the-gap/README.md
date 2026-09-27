# Mind the Gap

Un mini-jeu de vocabulaire anglais calé sur la façon dont la prof interroge :
**par évaluation**, et dans chaque évaluation par **groupes de mots**.

*Évaluation 1* réunit les quatre premiers groupes du cahier — *Greetings*,
*School stuff*, *Written instructions*, *Oral instructions* — soit 45 mots.
*Évaluation 2* en réunit trois — *Everyday needs*, les 13 phrases de classe du
*classroom English* ; *Colours*, les onze couleurs de la fiche ; *Almost
transparent words*, les 22 mots qui se devinent du français — soit 46 mots.
L'accueil montre une grande carte par évaluation ; on
l'ouvre pour trouver ses groupes, et chaque groupe se déplie sur les trois
modes.

Page unique, sans dépendance, sans réseau : `index.html`. Les progrès restent
dans le navigateur (`localStorage`), rien n'est envoyé nulle part.

## Les trois modes, dans cet ordre

| Mode | Ce qu'on demande | Tolérance |
|------|------------------|-----------|
| **Je choisis** | reconnaître le mot parmi trois | — |
| **Je le dis** | le dire à voix haute (micro, ou auto-évaluation si le micro n'est pas accessible) | l'article est facultatif, la phrase entière est acceptée |
| **Je l'écris** | le taper au clavier | **aucune** : casse, espaces et point final mis à part, chaque lettre compte, l'article compris |

Les groupes de phrases (*Everyday needs*) suivent la même règle avec une seule
souplesse : la virgule et le point d'interrogation sont facultatifs, mais
l'apostrophe ne l'est pas — `I dont know` est refusé, `Sorry I'm late` passe.
Une phrase longue s'affiche en minuscules sur la barre du roundel plutôt qu'en
capitales de signalétique, et la reconnaissance vocale desserre sa tolérance à
proportion de la longueur.

## Épeler

La prof veut que les mots soient épelés en anglais. Un bouton **ABC** donne le
modèle : chaque lettre est dite à son nom anglais pendant que sa tuile s'allume,
la lettre et le son ensemble, puis le mot entier est redit d'un trait. Un
second appui coupe — une phrase fait trente lettres.

On donne à la synthèse **la lettre elle-même, en capitale**. C'est le chemin
que les moteurs prévoient pour ça, et les 26 noms en sortent justes — vérifié
phonème par phonème contre espeak-ng en `en-gb`.

Il y avait ici une table phonétique — `ee` pour E, `ay` pour A, `eff` pour F —
et c'était une fausse bonne idée : ces suites ne sont pas des mots, alors
certaines voix les relisent lettre par lettre, d'où le double /iː/ entendu sur
le E de *lemonade*. Deux étaient franchement fausses : `ay` sort en /aɪ/, le
nom du **I**, et `eff` en /iːɛfɛf/, « E-F-eff ».

Un seul cas résiste : le **Z**, que les voix américaines appellent `zee`.
Quand aucune voix britannique n'est disponible, on écrit `zed` en toutes
lettres — qui se dit /zɛd/ des deux côtés de l'Atlantique.

Sans son, les tuiles défilent quand même : le rythme visuel reste.

Le bouton n'apparaît dans une partie **qu'une fois la réponse donnée**, jamais
avant, où il soufflerait le mot. Dans le carnet il est là en permanence, à côté
du haut-parleur, pour réviser.

## Orthographe britannique

Trois écarts fréquents sont nommés plutôt que comptés faux tout court :
`color` pour **colour**, `theater` pour **theatre**, `gray` pour **grey**. Le
message dit lequel ; la réponse reste fausse.

Un mot n'est « maîtrisé » que lorsqu'il est juste dans les trois modes, sans
indice. La barre en segments de la carte d'évaluation — un segment par groupe,
large comme son nombre de mots — ne remplit que ceux-là.

## Code parent

Un lien discret en bas de l'accueil ouvre un champ : le code **PARENTS** lève
tous les cadenas d'un coup — groupes et modes — et le même lien les remet.
C'est un garde-fou d'enfant, pas un secret : le code est écrit dans la page, et
c'est très bien ainsi. Il sert à réviser un groupe juste avant l'évaluation sans
avoir à repasser par les précédents. Le choix est gardé dans le navigateur, avec
le reste des progrès ; « Tout effacer » ne le remet pas.

## Ajouter une évaluation

Une entrée dans `EVALS`, puis ses groupes dans `LIGNES` avec le numéro de
l'évaluation :

```js
EVALS.push({id:2, nom:'Évaluation 2', zone:'Zone 2', sous:'…'});
// puis, dans LIGNES :
{id:5, ev:2, tok:'--l1', nom:'Numbers', sous:'…'},
{id:902, ev:2, tok:'--l0', tout:true, nom:'All change', sous:'…'}
```

`tok` désigne un jeton de couleur (`--l1` à `--l4`, `--l0` pour la révision) ;
les cinq se réutilisent d'une évaluation à l'autre, mais jamais deux fois dans
la même. `tout:true` marque la ligne
de révision, qui rebat douze mots au hasard parmi ceux de **son** évaluation —
elle reste cachée tant que l'évaluation n'a qu'un seul groupe, où elle ferait
doublon, et apparaît d'elle-même au deuxième.

Les identifiants de groupe ne se réutilisent jamais : ce sont les clés des
étoiles déjà gagnées. Chaque évaluation s'ouvre à son premier groupe — la prof
peut les donner dans l'ordre qu'elle veut.

## Ajouter des mots

Une ligne dans le tableau `MOTS` du script suffit :

```js
{id:'ruler', l:2, en:'a ruler', fr:'une règle', note:'', alt:[], svg:d('…')}
```

`l` est le numéro de leçon, `alt` les autres formes acceptées (`talk` pour
`speak`), `note` la précision qui lève une ambiguïté (`regarde` *(une vidéo)*).
Stations, QCM, carnet et compteurs s'y adaptent seuls.

Quand un groupe reprend des mots déjà vus — la fiche *Oral instructions*
redemande `read`, `listen` et `write` de *Written instructions* — on les cite
dans son champ `aussi` plutôt que de les récrire :

```js
{id:4, nom:'Oral instructions', sous:'…', aussi:['read','listen','write']}
```

Ils rejouent dans ce groupe et le carnet signale d'où ils viennent, mais ils
n'existent qu'une fois dans `MOTS` : le compteur de mots maîtrisés ne les compte
donc jamais deux fois. Le champ `rem` affiche une remarque sous le titre du
groupe dans le carnet.

## Dessins

80 pictogrammes au trait, redessinés d'après les fiches du cahier. Ils prennent
leurs couleurs des jetons CSS : les deux thèmes suivent.

Les onze couleurs font exception, forcément : une tache « rouge » doit rester
rouge en clair comme en sombre. `tache('#e03127')` pose la teinte en dur et ne
laisse au thème que le contour, ce qui garde le noir et le blanc lisibles des
deux côtés. Le blanc prend en plus un fond gris, comme sur la fiche, sans quoi
il disparaîtrait sur la carte.
