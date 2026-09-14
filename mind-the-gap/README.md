# Mind the Gap

Un mini-jeu de vocabulaire anglais pour réviser les trois premières leçons du
cahier : *Greetings*, *School stuff*, *Written instructions* — 36 mots.

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

## Dessins

36 pictogrammes au trait, redessinés d'après la fiche « Instructions » de la
leçon 3. Ils prennent leurs couleurs des jetons CSS : les deux thèmes suivent.
