#!/usr/bin/node
exports.executeNTimes = function (x, theFunction) {
  for (let i = 0; i < x; i++) theFunction();
};
