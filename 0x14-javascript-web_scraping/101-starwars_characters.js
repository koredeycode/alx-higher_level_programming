#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    print(characters, 0);
  }
});

function print (characters, index) {
  request(characters[index], (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        print(characters, index + 1);
      }
    }
  });
}
