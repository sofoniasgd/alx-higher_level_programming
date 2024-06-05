#!/usr/bin/node

const args = process.argv;

const request = require('request');

const url = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + args[2],
  method: 'GET'
};

request(url, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  const bJson = JSON.parse(body);
  console.log(bJson.title);
});
