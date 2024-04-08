#!/usr/bin/node
const commandArgs = process.argv;
const firstArgument = Number(commandArgs[2]);
let text = '';

if (!firstArgument) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArgument; i++) {
    text += 'x';
  }
  for (let j = 0; j < firstArgument; j++) {
    console.log(text);
  }
}
