#!/usr/bin/node
const commandArgs = process.argv;
const firstArgument = Number(commandArgs[2]);
const text = 'C is fun';

if (!firstArgument) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < firstArgument; i++) {
    console.log(text);
  }
}
