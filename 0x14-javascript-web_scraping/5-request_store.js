#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (err, response, body) {
  if (err === null && response.statusCode === 200) {
    fs.writeFileSync(process.argv[3], body, 'utf-8');
    console.log(`Contents of ${process.argv[2]} have been saved to ${process.argv[3]}`);
  } else {
    console.error(err || `Failed to fetch ${process.argv[2]}. Status code: ${response.statusCode}`);
  }
});
