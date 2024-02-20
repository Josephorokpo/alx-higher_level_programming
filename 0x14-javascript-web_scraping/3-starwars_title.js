#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie. Status code: ${response.statusCode}`);
    return;
  }

  const movieData = JSON.parse(body);
  console.log(`Title: ${movieData.title}`);
});
