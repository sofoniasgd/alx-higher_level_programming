#!/usr/bin/node

const args = process.argv;

const request = require('request');

const url = {
  url: args[2],
  method: 'GET'
};

request(url, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  console.log('code:', response.statusCode);
});
