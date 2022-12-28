const http = require('http');
// const fs = require('fs');

const express = require('express');
const json2html = require('node-json2html');
// const app = express();

// Array mit moeglichen Klassen usw. (siehe oben)
const classes = ['Krieger', 'Magier', 'Dieb', 'Druide', 'Barden', 'Priester'];
const races = ['Mensch', 'Elf', 'Zwerg', 'Halbelf', 'Halbling', 'Ork','Troll', 'Goblin', 'Nachelfen'];
const genders = ['maennlich', 'weiblich'];
const property_positiv = ['Mitfuehlend',
    'Loyal', 
    'Einfuehlsam',
    'Verantwortungsbewusst',
    'Zuvorkommend',
    'Ehrlich',
    'Verlaesslich',
    'Selbstlos',
    'Aufmerksam',
    'Entgegenkommend',
    'Barmherzig',
    'Großzuegig',
    'Tolerant',
    'Respektvoll',
    'Hoeflich',
    'Geduldig',
    'Mitgefuehl',
    'Verstaendnisvoll',
    'Mitfuehlend',
    'Großherzig',
    'Guetig',
    'Freundlich',
  ]
const property_negativ = ['Arrogant',
    'Egoist',
    'Gierig',
    'Intolerant',
    'Neidisch',
    'Rassist',
    'Vorurteilbehaftet',
    'Selbstsuechtig',
    'Eifersuechtig',
    'Ruecksichtslosigkeit',
    'Intoleranz',
    'Unfreundlichkeit',
    'Unaufrichtigkeit',
    'Eitelkeit',
    'Unbesonnenheit',
    'Ungerechtigkeit',
    'Unbarmherzigkeit',
    'Unbescheidenheit',
    'Unverschaemtheit',
    'Unhoeflichkeit',
    'Ungehobeltheit',
    'Unzufriedenheit',
    'Unentschlossenheit',
    'Unachtsamkeit',
    'Unaufmerksamkeit',
    'Unzuverlaessigkeit',
    'Undankbarkeit',
    'Ungehorsam',
  ]

// Funktion zum Generieren zufaelliger Werte aus einem Array (siehe oben)
function getRandomValueFromArray(array) {
  return array[Math.floor(Math.random() * array.length)];
}

// Funktion zum Generieren eines DSA-Charakters (siehe oben)
function generateCharacter() {
  const charClass = getRandomValueFromArray(classes);
  const charRace = getRandomValueFromArray(races);
  const charGender = getRandomValueFromArray(genders);
  const charproperty_postiv1 = getRandomValueFromArray(property_positiv);
  const charproperty_postiv2 = getRandomValueFromArray(property_positiv);
  const charproperty_postiv3 = getRandomValueFromArray(property_positiv);

  const charproperty_negativ1 = getRandomValueFromArray(property_negativ);
  const charproperty_negativ2 = getRandomValueFromArray(property_negativ);
  const charproperty_negativ3 = getRandomValueFromArray(property_negativ);

  /*
  const attributes = {
    str: Math.ceil(Math.random() * 20),
    dex: Math.ceil(Math.random() * 20),
    con: Math.ceil(Math.random() * 20),
    int: Math.ceil(Math.random() * 20),
    wis: Math.ceil(Math.random() * 20),
    cha: Math.ceil(Math.random() * 20)
  };
  */
  return {
    class: charClass,
    race: charRace,
    gender: charGender,
    positiv_traits1: charproperty_postiv1,
    positiv_traits2: charproperty_postiv2,
    positiv_traits3: charproperty_postiv3,
    negativ_traits1: charproperty_negativ1,
    negativ_traits2: charproperty_negativ2,
    negativ_traits3: charproperty_negativ3,
    // attributes: attributes
  };
}

const server = http.createServer((req, res) => {
  // Verarbeite nur Anforderungen an die URL "/hello"
  if (req.url === '/' && req.method === 'GET') {

    // Rufe die Funktion auf, die das JSON generiert
    let template = { '<>':'div','html':[
      { '<>':'div','text':'Klasse: ${class}' },
      { '<>':'div','text': 'Rasse: ${race}' },
      { '<>':'div','text': 'Charaktereigenschaften:' },
      { '<>':'div','html': [
          { '<>':'li','text':'${positiv_traits1}' },
          { '<>':'li','text':'${positiv_traits2}' },
          { '<>':'li','text':'${positiv_traits3}' },
          { '<>':'li','text':'${negativ_traits1}' },
          { '<>':'li','text':'${negativ_traits2}' },
          { '<>':'li','text':'${negativ_traits3}' }
        ]},
      ]};
    let json = generateCharacter();

    // Wandle das JSON in HTML um
    let html = json2html.render(json,template);

    // Sende das HTML zurueck an den Client
    res.end(html);
    res.statusCode = 200;
  } else {
    res.statusCode = 302;
    res.setHeader('location', '/');
    return res.end();
    // res.statusCode = 404;
    // res.end('404, not nound\n');
  }
});

server.listen(3000, () => {
  console.log('Server listening on port 3000');
});