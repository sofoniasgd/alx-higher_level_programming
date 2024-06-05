#!/usr/bin/node

const request = require('request');

const url = {
  url: 'https://swapi-api.alx-tools.com/api/films',
  method: 'GET'
};

let bJson, films, charList;
// character id for “Wedge Antilles”
const id = 18;

request(url, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  bJson = JSON.parse(body);
  console.log('bJson type:',typeof(bJson));
  films = bJson.results;
  console.log('films:',typeof(films));

  charList = films.characters;
  console.log('charList:', charList);
  
  //charList.forEach(function (result) {
    //console.log(result);
  //});

});
