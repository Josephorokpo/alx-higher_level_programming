#!/usr/bin/node

const dict = require('./101-data').dict;

function invertDictionary(originalDict) {
  const invertedDict = {};

  Object.keys(originalDict).forEach(key => {
    const occurrences = originalDict[key];

    invertedDict[occurrences] = invertedDict[occurrences] || [];

    invertedDict[occurrences].push(key);
  });

  return invertedDict;
}

const newDict = invertDictionary(dict);

console.log(newDict);
