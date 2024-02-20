#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;

    charactersUrls.forEach(characterUrl => {
      request(characterUrl, function (err, resp, body) {
        if (!err && resp.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  }
});
