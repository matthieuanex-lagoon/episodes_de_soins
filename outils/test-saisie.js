/* Vérifie la comparaison tolérante du mode « J'écris le nom ».
 *
 *   node outils/test-saisie.js
 *
 * Les fonctions ne sont pas recopiées ici : elles sont extraites de
 * jeu-materiel-tp/index.html à chaque exécution, pour que le test ne puisse
 * pas dériver de ce que le jeu fait réellement. */

const fs = require('fs');
const path = require('path');
const src = fs.readFileSync(path.join(__dirname, '..', 'jeu-materiel-tp', 'index.html'), 'utf8');

function extraire(re, quoi){
  const m = src.match(re);
  if(!m) throw new Error('introuvable dans index.html : ' + quoi);
  return m[0];
}
const morceaux = [
  'var ITEMS = [' +
    [...src.matchAll(/\{id:'(\w+)', nom:'([^']*)',/g)]
      .map(m => `{id:'${m[1]}', nom:'${m[2]}'}`).join(', ') + '];',
  extraire(/var MOTS_VIDES = [\s\S]*?\n.*?\];/, 'MOTS_VIDES'),
  extraire(/var RACCOURCIS = \{[\s\S]*?\n\};/, 'RACCOURCIS'),
  ...['normaliser','lev','variantes','tolerance','juger',
      'echapper','lettres','diffMot','motsUtiles','marquerFautes']
      .map(f => extraire(new RegExp('function ' + f + '\\([\\s\\S]*?\\n\\}'), f))
];
const { ITEMS, juger, marquerFautes } = new Function(morceaux.join('\n') +
  '\nreturn {ITEMS, juger, marquerFautes};')();

const parId = id => {
  const it = ITEMS.find(x => x.id === id);
  if(!it) throw new Error('objet inconnu : ' + id);
  return it;
};

/* Doivent passer sans la moindre remarque : seuls les accents, les
   particules, les pluriels, les espaces et les raccourcis d'usage varient. */
const JUSTE = [
  ['becher','Bécher'],['becher','becher'],['becher','BECHER'],['becher','bêcher'],
  ['tube','Tube à essai'],['tube','tube a essai'],['tube','tube essai'],['tube','tubes à essais'],['tube','tube'],
  ['petri','Boîte de Pétri'],['petri','boite de petri'],['petri','boite petri'],['petri','petri'],['petri','boite de pétris'],
  ['erlen','erlenmeyer'],['erlen','erlen'],['erlen','erlenmeyer '],
  ['eprouvette','Éprouvette graduée'],['eprouvette','eprouvette'],
  ['comptegoutte','Pipette compte-gouttes'],['comptegoutte','compte goutte'],['comptegoutte','compte-gouttes'],
  ['portetubes','Porte-tubes à essai'],['portetubes','porte tube'],['portetubes','portoir'],['portetubes','porte tubes a essai'],
  ['lame','Lame et lamelle'],['lame','lame + lamelle'],['lame','lame lamelle'],['lame','lamelle'],
  ['chauffeballon','Chauffe-ballon'],['chauffeballon','chauffe ballon'],
  ['bainmarie','Bain-marie'],['bainmarie','bain marie'],['bainmarie','bain-marie'],
  ['verrepied','Verre à pied'],['verrepied','verre a pied'],['verrepied','verre pied'],
  ['verremontre','Verre de montre'],['verremontre','verre montre'],['verremontre','verre de montres'],
  ['cristallisoir','Cristallisoir'],
  ['capsule','Capsule de pesée'],['capsule','capsule'],['capsule','capsule de pesee'],
  ['balance','Balance électronique'],['balance','balance'],['balance','balance electronique'],
  ['pissette','Pissette à eau'],['pissette','pissette'],
  ['fiole','Fiole jaugée'],['fiole','fiole'],['fiole','fiole jaugee'],
  ['pince','Pince fine'],['pince','pince'],['pince','brucelles'],
  ['pipette','Pipette'],['ballon','Ballon'],['entonnoir','Entonnoir'],
  ['tube','tubeaessai'],['comptegoutte','comptegouttes'],
];

/* Le bon objet, mais mal écrit : acceptés, et signalés. */
const ORTHO = [
  ['erlen','Erlenmayer'],['erlen','erlenmyer'],
  ['eprouvette','eprouvete graduee'],['eprouvette','eprouvete'],
  ['cristallisoir','cristalisoir'],['cristallisoir','cristalisoire'],
  ['entonnoir','entonoir'],['becher','becheur'],['balance','balence'],
  ['pissette','pisette a eau'],['bainmarie','bain marrie'],
];

/* Doivent être refusés : les mots à cheval sur deux objets, et les
   ressemblances trompeuses que la seule distance d'édition laisserait passer. */
const FAUX = [
  ['verrepied','verre'],['verremontre','verre'],
  ['comptegoutte','pipette'],['pipette','pissette'],['pissette','pipette'],
  ['portetubes','tube'],['chauffeballon','ballon'],['ballon','chauffe-ballon'],
  ['becher',''],['becher','bidule'],['erlen','entonnoir'],['petri','cristallisoir'],
  ['tube','tube a essai renverse par terre'],['lame','lamelle de microscope tres fine et cassee'],
  ['chauffeballon','chofe balon'],['eprouvette','eprvette'],['becher','bcher x'],
];

/* Ce qui doit être souligné en rouge : lettre fausse, lettre en trop,
   et « · » là où une lettre a été oubliée. */
const MARQUES = [
  ['erlen','erlenmayer',   'erlenm<span class="faute">a</span>yer'],
  ['entonnoir','entonoir', 'enton<span class="manque">·</span>oir'],
  ['becher','becheur',     'beche<span class="faute">u</span>r'],
];

let ko = 0;
for(const [id, txt] of JUSTE){
  const v = juger(txt, parId(id));
  if(v !== 'juste'){ ko++; console.log('✗ devait passer sans remarque :', JSON.stringify(txt), '→', id, '| verdict', v); }
}
for(const [id, txt] of ORTHO){
  const v = juger(txt, parId(id));
  if(v !== 'presque'){ ko++; console.log('✗ devait être signalé :', JSON.stringify(txt), '→', id, '| verdict', v); }
}
for(const [id, txt] of FAUX){
  const v = juger(txt, parId(id));
  if(v !== 'faux'){ ko++; console.log('✗ devait échouer :', JSON.stringify(txt), '→', id, '| verdict', v); }
}
for(const [id, txt, attendu] of MARQUES){
  const h = marquerFautes(txt, parId(id));
  if(h !== attendu){ ko++; console.log('✗ balisage :', JSON.stringify(txt), '\n     obtenu', JSON.stringify(h), '\n   attendu', JSON.stringify(attendu)); }
}
const total = JUSTE.length + ORTHO.length + FAUX.length + MARQUES.length;
console.log(ko === 0 ? `\n✓ ${total} cas, tous conformes` : `\n${ko} écart(s) sur ${total} cas`);
process.exit(ko === 0 ? 0 : 1);
