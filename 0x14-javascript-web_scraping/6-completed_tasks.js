#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const toDos = JSON.parse(body);
    const obj = {};

    for (const toDo of toDos) {
      if (toDo.completed === true) {
        const uid = toDo.userId;
        obj[uid] ? obj[uid] += 1 : obj[uid] = 1;
      }
    }
    console.log(obj);
  }
});
