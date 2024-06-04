#!/usr/bin/node

const args = process.argv;

// use fs to read file
const fs = require('fs');

fs.readFile(args[2], 'utf-8', function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.log(data);
});
