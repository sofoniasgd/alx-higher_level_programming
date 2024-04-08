#!/usr/bin/node
const cmdarguments = process.argv;
const num = Number(cmdarguments[2]);

function factorial (a) {
  if (!a || a === 0) {
    return 1;
  }
  if (a > 0) {
    return a * factorial(a - 1);
  }
}
console.log(factorial(num));
