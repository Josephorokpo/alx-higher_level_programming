#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      const characters = film.characters;
      for (const character of characters) {
        if (character.includes('18')) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  } else {
    console.error('An error occurred. Status code: ' + response.statusCode);
  }
});
