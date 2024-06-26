#!/usr/bin/node

const request = require('request');
const args = process.argv;

const url = {
  url: args[2]
};

let bJson, films, charList;
let occurence = 0;

// character id for “Wedge Antilles” is '18'
const id = '18';

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
      // split character string to get chracer id
      const carr = character.split('/');
      if (carr[carr.length - 2] === id) {
        occurence++;
      }
    });
  });
  console.log(occurence);
});
