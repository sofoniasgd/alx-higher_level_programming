#!/usr/bin/node

const args = process.argv;

// use fs to write file
const fs = require('fs');

fs.writeFile(args[2], args[3], 'utf-8', function (err) {
  if (err) {
    return console.error(err);
  }
});
