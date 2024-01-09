#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Use the reduce function to count occurrences
  const occurrences = list.reduce(function (count, element) {
    // Increment count when the element matches the searchElement
    return count + (element === searchElement);
  }, 0);

  return occurrences;
};
