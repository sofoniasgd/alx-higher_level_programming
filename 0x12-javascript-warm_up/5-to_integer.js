#!/usr/bin/node
const commandArgs = process.argv;
const firstArgument = Number(commandArgs[2]);
if (firstArgument) {
  console.log('My number: ' + firstArgument);
} else {
  console.log('Not a number');
}
