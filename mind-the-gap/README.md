# Parlez-vous ?

Deux cours de langues dans une seule page, calés sur la façon dont les profs
interrogent : **par évaluation**, et dans chaque évaluation par **groupes de
mots**.

| Cours | Langue | Contenu |
|-------|--------|---------|
| **Mind the Gap** | anglais | 2 évaluations, 9 groupes, 122 mots |
| **Sprichst du Deutsch?** | allemand | 1 évaluation, 3 groupes, 55 mots |

L'écran d'entrée pose la question et les deux cartes y répondent. On ouvre un
cours sur ses évaluations, une évaluation sur ses groupes, et chaque groupe se
déplie sur les trois modes.

Page unique, sans dépendance, sans réseau : `index.html`. Les progrès restent
dans le navigateur (`localStorage`), rien n'est envoyé nulle part.

## Les trois modes, dans cet ordre

| Mode | Ce qu'on demande | Tolérance |
|------|------------------|-----------|
| **Je choisis** | reconnaître le mot parmi trois | — |
| **Je le dis** | le dire à voix haute (micro, ou auto-évaluation si le micro n'est pas accessible) | l'article est facultatif, la phrase entière est acceptée |
| **Je l'écris** | le taper au clavier | **aucune** : casse, espaces et point final mis à part, chaque lettre compte |

Un mot n'est « maîtrisé » que lorsqu'il est juste dans les trois modes, sans
indice. La barre en segments de la carte d'évaluation — un segment par groupe,
large comme son nombre de mots — ne remplit que ceux-là.

Les groupes de phrases suivent la même règle avec une seule souplesse : la
virgule et le point d'interrogation sont facultatifs, mais l'apostrophe ne
l'est pas — `I dont know` est refusé, `Sorry I'm late` passe. Une phrase longue
s'affiche en minuscules sur la barre du roundel plutôt qu'en capitales de
signalétique, et se resserre encore au-delà de quarante-deux caractères.

## Épeler

Les deux profs veulent que les mots soient épelés dans leur langue. Un bouton
**ABC** donne le modèle : chaque lettre est dite à son nom pendant que sa tuile
s'allume, la lettre et le son ensemble, puis le mot entier est redit d'un
trait. Un second appui coupe — une phrase fait trente lettres.

On donne à la synthèse **la lettre elle-même**, avec la langue du cours. C'est
le chemin que les moteurs prévoient pour ça, et les noms en sortent justes de
part et d'autre : le même `A` se dit /eɪ/ en `en-GB` et /aː/ en `de`. Vérifié
phonème par phonème contre espeak-ng, les 26 lettres plus `Ä Ö Ü ß`.

**On prononce la minuscule et on affiche la capitale.** Les deux donnent le
même nom de lettre — l'article `a` anglais compris — mais une capitale isolée
fait annoncer « capital A », « großes A » à beaucoup de voix. Ce préfixe
n'apprend rien, et il allongeait chaque lettre au point de dépasser le
garde-fou qui rattrape les voix ne rappelant pas `onend` : la parole était
coupée puis relancée, et on entendait le préfixe en boucle. Le test vérifie
désormais qu'aucune capitale isolée ne part à la synthèse.

Il y avait ici une table phonétique — `ee` pour E, `ay` pour A, `eff` pour F —
et c'était une fausse bonne idée : ces suites ne sont pas des mots, alors
certaines voix les relisent lettre par lettre, d'où le double /iː/ entendu sur
le E de *lemonade*. Deux étaient franchement fausses : `ay` sort en /aɪ/, le
nom du **I**, et `eff` en /iːɛfɛf/, « E-F-eff ».

Deux exceptions subsistent :

- le **Z**, que les voix américaines appellent `zee` ; faute de voix
  britannique on écrit `zed`, qui se dit /zɛd/ des deux côtés de l'Atlantique ;
- le **ß**, qui n'a pas de capitale : `majLettre()` le laisse tel quel, sans
  quoi `toUpperCase()` en ferait « SS », deux lettres là où la tuile n'en
  montre qu'une.

Dans une partie, le bouton n'apparaît **qu'une fois la réponse donnée**, jamais
avant, où il soufflerait le mot. Dans le carnet il est là en permanence.

## Les trémas, et le clavier français

Un clavier AZERTY ne donne ni `ä` ni `ß` — or le mode « Je l'écris » ne tolère
aucune faute. Sans rien faire, la moitié des nombres allemands (**fünf**,
**zwölf**, **dreißig**) serait intapable. Deux réponses :

- une rangée de touches **ä ö ü ß** sous le champ, qui insèrent au point
  d'insertion sans effacer ce qui est déjà écrit ;
- la substitution officielle `ae oe ue ss`, acceptée des deux côtés de la
  comparaison : `fuenf` passe, `funf` non.

Quand seul le tréma manque, le message le nomme : « il manque le tréma — **ü**,
ou **ue** au clavier français ». La réponse reste fausse ; c'est le tréma qu'on
apprend.

## La majuscule

Les jours, les mois et les nationalités prennent une majuscule en anglais ; en
allemand, **tous les noms** la prennent. Le français n'en met nulle part.

La casse n'a jamais compté ici et ce n'est pas le moment de changer la règle :
`monday` et `fussball` restent **justes**, le jeu ajoute seulement « au
passage : en anglais, **Monday** prend une majuscule ».

Le champ `cap:true` marque les entrées concernées. Sur une phrase, le premier
mot est sauté — sa majuscule ne dit rien de la langue, elle dit seulement
qu'une phrase commence ; c'est `France` qu'on veut signaler dans *I am from
France*, pas `I`, et `Fußball` dans *Ich spiele gern Fußball*, pas `Ich`. Les
saisons anglaises et les nombres allemands ne sont pas marqués : ils restent en
minuscules.

## Orthographe

Quatre écarts fréquents sont nommés plutôt que comptés faux tout court :
`color` pour **colour**, `theater` pour **theatre**, `gray` pour **grey**, et
le tréma manquant. Le message dit lequel ; la réponse reste fausse.

Côté allemand, la fiche écrit *Fussball* et *Hobbies* là où l'orthographe
moderne dit *Fußball* et *Hobbys* : les deux premières passent, `alt` porte la
variante. Les pièges des nombres sont dans les notes du groupe — **sechzehn**
perd son *s*, **siebzehn** son *en*, **dreißig** prend l'eszett.

## Code parent

Un lien discret en bas de l'écran d'entrée ouvre un champ : le code **PARENTS**
lève tous les cadenas d'un coup — les deux cours, tous les groupes, tous les
modes — et le même lien les remet. C'est un garde-fou d'enfant, pas un secret :
le code est écrit dans la page, et c'est très bien ainsi. Il sert à réviser un
groupe juste avant l'évaluation sans avoir à repasser par les précédents.

## Ajouter un cours

Une entrée dans `COURS` :

```js
{id:'es', nom:'¿Hablas español?', adj:'espagnol', langue:'Espagnol', lang:'es-ES',
 sous:'…', bravos:['¡Bien!','¡Genial!',…], rate:'¡Cuidado!', aide:'Con ayuda'}
```

`lang` sert à la synthèse vocale, à la reconnaissance vocale **et** aux noms de
lettres du bouton ABC : les trois suivent automatiquement. `rate`, `aide` et
`bravos` passent par `textContent`, donc ils s'écrivent avec de vrais
caractères accentués, pas des entités.

Un habillage propre au cours s'ajoute en CSS sous `body.cours-<id>` — c'est là
que l'allemand échange le roundel londonien contre le carré du U-Bahn et le
bleu contre le jaune BVG :

```css
body.cours-de{--barre:#f0d722; --barre-txt:#17140a}
body.cours-de .roundel{border-radius:15%}
```

## Ajouter une évaluation, un groupe, des mots

```js
EVALS.push({id:102, co:'de', nom:'Évaluation 2', zone:'Bereich B', sous:'…'});
// puis, dans LIGNES :
{id:104, ev:102, tok:'--d1', nom:'Farben', sous:'…'},
{id:952, ev:102, tok:'--l0', tout:true, nom:'Alles umsteigen', sous:'…'}
// puis, dans MOTS :
{id:'de-rot', l:104, en:'rot', fr:'rouge', svg:d('…')}
```

Le cours d'un mot se déduit : mot → ligne → évaluation → cours. Rien n'est
écrit deux fois, et un mot ne peut pas se retrouver dans la mauvaise langue.

`tok` désigne un jeton de couleur : `--l1` à `--l5` pour les lignes de Londres,
`--d1` à `--d3` pour celles de Berlin, `--l0` pour la révision. Ils se
réutilisent d'une évaluation à l'autre, jamais deux fois dans la même.
`tout:true` marque la ligne de révision, qui rebat douze mots au hasard parmi
ceux de **son** évaluation — elle reste cachée tant que l'évaluation n'a qu'un
seul groupe, où elle ferait doublon.

Les identifiants ne se réutilisent jamais, ni entre groupes ni entre mots : ce
sont les clés des étoiles et des acquis déjà gagnés. Les mots allemands sont
préfixés `de-` pour que la question ne se pose pas.

`alt` liste les autres formes acceptées (`talk` pour `speak`, `fall` pour
`autumn`), `note` la précision qui lève une ambiguïté (`regarde` *(une
vidéo)*), `rem` une remarque affichée sous le titre du groupe dans le carnet.

Quand un groupe reprend des mots déjà vus — la fiche *Oral instructions*
redemande `read`, `listen` et `write` de *Written instructions* — on les cite
dans son champ `aussi` plutôt que de les récrire : ils rejouent dans ce groupe,
le carnet signale d'où ils viennent, et le compteur ne les compte jamais deux
fois.

## Dessins

166 pictogrammes au trait, redessinés d'après les fiches des cahiers. Ils
prennent leurs couleurs des jetons CSS : les deux thèmes suivent.

Trois familles font exception, forcément :

- **les onze couleurs anglaises** — une tache « rouge » doit rester rouge en
  clair comme en sombre. `tache('#e03127')` pose la teinte en dur et ne laisse
  au thème que le contour ; le blanc prend en plus un fond gris, comme sur la
  fiche ;
- **les drapeaux** britannique et français, même règle ;
- **le carré du U-Bahn**, bleu dans les deux thèmes, d'où le blanc posé en dur
  sur son numéro.

Trois familles sont générées plutôt que dessinées, parce que ce qui distingue
leurs membres est un rang ou un nombre, pas une image :

- `jourSem(n)` et `moisAn(n)` montrent la case occupée dans la semaine ou dans
  l'année — et ça apprend au passage que *September* est le neuvième mois ;
- `zahl(n)` pose le chiffre dans le carré du U-Bahn. Montrer « 7 » ne souffle
  rien : c'est *sieben* qu'on cherche.

## Le prénom n'est pas dans le dépôt

*About me* reprend la page de présentation du cahier d'anglais, mais en
tournures : `My name is...` et non le prénom, parce que le dépôt est public et
que c'est la tournure qui s'apprend. L'âge et le pays sont, eux, ceux de la
fiche.

## Le dossier s'appelle encore `mind-the-gap`

Il héberge maintenant les deux cours, mais l'URL GitHub Pages et celle de
l'artifact Claude sont liées à ce chemin. Renommer casserait les deux liens
pour un gain cosmétique : on garde.
