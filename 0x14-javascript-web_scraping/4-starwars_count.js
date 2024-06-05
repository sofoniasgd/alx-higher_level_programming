#!/usr/bin/node

const request = require('request');

const url = {
  url: 'https://swapi-api.alx-tools.com/api/films',
  method: 'GET'
};

let bJson, films, charList;
let occurence = 0;

// character id for “Wedge Antilles” is '18'

request(url, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  bJson = JSON.parse(body);
  films = bJson.results;

  films.forEach(function (result) {
    // character id list
    charList = result.characters;
    // seach for the character id in every films character list
    charList.forEach(function (character) {
      if (character.substr(43) === '18/') {
        occurence++;
      }
    });
  });
  console.log(occurence);
});
