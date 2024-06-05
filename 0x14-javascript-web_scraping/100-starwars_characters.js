#!/usr/bin/node

const args = process.argv;
const request = require('request');

const url = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + args[2]
};
request(url, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  const json = JSON.parse(body);
  // get character id list
  const characters = json.characters;

  characters.forEach(function (cId) {
    // do a request for each entry to get the character name
    request(cId, (error, response, body) => {
      if (error) {
        return console.error(error);
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});