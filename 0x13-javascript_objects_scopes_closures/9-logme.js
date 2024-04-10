#!/usr/bin/node
let myVar = 0;

exports.logMe = function (item) {
  console.log(myVar + ': ' + item);
  myVar += 1;
};
