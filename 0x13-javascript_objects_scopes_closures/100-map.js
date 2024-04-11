#!/usr/bin/node
const list = require('./100-data.js').list;
let index = 0;
const newList = list.map((x) => (x * index++));
console.log(list);
console.log(newList);
