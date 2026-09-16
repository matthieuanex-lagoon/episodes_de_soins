# Mind the Gap

Un mini-jeu de vocabulaire anglais pour réviser les quatre premières leçons du
cahier : *Greetings*, *School stuff*, *Written instructions*, *Oral instructions*
— 45 mots.

Page unique, sans dépendance, sans réseau : `index.html`. Les progrès restent
dans le navigateur (`localStorage`), rien n'est envoyé nulle part.

## Les trois modes, dans cet ordre

| Mode | Ce qu'on demande | Tolérance |
|------|------------------|-----------|
| **Je choisis** | reconnaître le mot parmi trois | — |
| **Je le dis** | le dire à voix haute (micro, ou auto-évaluation si le micro n'est pas accessible) | l'article est facultatif, la phrase entière est acceptée |
| **Je l'écris** | le taper au clavier | **aucune** : casse, espaces et point final mis à part, chaque lettre compte, l'article compris |

Un mot n'est « maîtrisé » que lorsqu'il est juste dans les trois modes, sans
indice. Le compteur de la page d'accueil ne compte que ceux-là.

## Ajouter des mots

Une ligne dans le tableau `MOTS` du script suffit :

```js
{id:'ruler', l:2, en:'a ruler', fr:'une règle', note:'', alt:[], svg:d('…')}
```

`l` est le numéro de leçon, `alt` les autres formes acceptées (`talk` pour
`speak`), `note` la précision qui lève une ambiguïté (`regarde` *(une vidéo)*).
Stations, QCM, carnet et compteurs s'y adaptent seuls.

Une nouvelle leçon s'ajoute dans `LIGNES`. Quand elle reprend des mots déjà vus
— la fiche *Oral instructions* redemande `read`, `listen` et `write` de la leçon
3 — on les cite dans son champ `aussi` plutôt que de les récrire :

```js
{id:4, nom:'Oral instructions', sous:'…', aussi:['read','listen','write']}
```

Ils rejouent dans la leçon 4 et le carnet signale d'où ils viennent, mais ils
n'existent qu'une fois dans `MOTS` : le compteur de mots maîtrisés ne les compte
donc jamais deux fois. Le champ `rem` affiche une remarque sous le titre de la
leçon dans le carnet.

## Dessins

45 pictogrammes au trait, redessinés d'après les fiches du cahier. Ils prennent leurs couleurs des jetons CSS : les deux thèmes suivent.
