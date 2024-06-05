#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const args = process.argv;

const url = {
  url: args[2]
};

request(url, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  // write the body of the page into file
  fs.writeFile(args[3], body, 'utf-8', function (err) {
    if (err) {
      return console.error(err);
    }
  });
});
