#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    const user = 'https://swapi-api.alx-tools.com/api/people/18/';
    for (const film of films) {
      if (film.characters.includes(user)) {
        count = count + 1;
      }
    }
    console.log(count);
  }
});
