#!/usr/bin/node

const args = process.argv;
const request = require('request');

// create new dictionary to store tasks complete
// by each employee
const eId = {
};

const url = {
  url: args[2]
};
request(url, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  const json = JSON.parse(body);
  json.forEach(function (task) {
    const uId = task.userId;
    if (uId in eId && task.completed === true) {
      eId[uId] += 1;
    } else if (!(uId in eId) && task.completed === true) {
      eId[uId] = 1;
    }
  });
  console.log(eId);
});
