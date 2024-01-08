#!/usr/bin/node

const numbers = process.argv.slice(2).map(Number);

numbers.sort((a, b) => b - a);

const secondBiggest = numbers[1] || 0;

console.log(secondBiggest);
