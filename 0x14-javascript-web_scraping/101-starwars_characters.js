#!/usr/bin/node

const args = process.argv;
const request = require('request');

let urlList = [];
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
  characters.forEach(function (url) {
    urlList.push(url);
  });
  function sequentialReq(urlList, index = 0) {
    if (index < characters.length) {
      request(urlList[index], (error, response, body) => {
        if (error) {
          return console.error(error);
        }
	const character = JSON.parse(body);
	console.log(character.name);
	
	sequentialReq(urlList, index + 1);
      });
    }
  }
	console.log(urlList);
});
