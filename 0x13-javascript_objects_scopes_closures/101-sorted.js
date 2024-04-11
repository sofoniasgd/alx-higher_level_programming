#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};

let occurence;
let found = false;
for (const key in dict) {
  occurence = dict[key];
  for (const key2 in newDict) {
    // search occurence in new dict
    if (key2 === occurence) {
      found = true;
      break;
    }
  }
  // if found occurence in newdict, do nothing else add occurence to newdict
  if (found === false) {
    newDict[occurence] = [];
  }
  found = false;
}
for (const key in newDict) {
  for (const id in dict) {
    if (Number(key) === dict[id]) {
      newDict[key].push(id);
    }
  }
}
console.log(newDict);
