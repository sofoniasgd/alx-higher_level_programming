#!/usr/bin/node
const cmdarguments = process.argv;
const a = Number(cmdarguments[2]);
const b = Number(cmdarguments[3]);
add(a, b);
function add (a, b) {
  console.log(a + b);
}
