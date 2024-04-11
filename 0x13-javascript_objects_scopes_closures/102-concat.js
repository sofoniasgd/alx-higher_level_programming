#!/usr/bin/node
const fs = require('fs');
if (process.argv.length === 5) {
  // write first file
  let data = fs.readFileSync(process.argv[2], 'utf-8');
  fs.writeFileSync(process.argv[4], data);
  // append second file data
  data = fs.readFileSync(process.argv[3], 'utf-8');
  fs.appendFileSync(process.argv[4], data);
}
