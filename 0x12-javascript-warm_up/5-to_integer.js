#!/usr/bin/node

const num = parseInt(process.argv[2]);

const output = isNaN(num) ? "Not a number" : `My number: ${num}`;

console.log(output);
