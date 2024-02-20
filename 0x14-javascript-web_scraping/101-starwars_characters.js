#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }
  request(characters[index], function (error, response, body) {
    if (!error && response.statusCode === 200) {
      console.log(JSON.parse(body).name);
      printCharacters(characters, index + 1);
    }
  });
}
