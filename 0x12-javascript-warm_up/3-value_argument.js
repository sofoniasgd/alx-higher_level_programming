#!/usr/bin/node
const commandArguments = process.argv;

if (!commandArguments[2]) {
  console.log('No argument');
} else {
  console.log(commandArguments[2]);
}
