#!/usr/bin/node

exports.esrever = function (list) {
  // Clone the original list to avoid modifying it directly
  const reversedList = list.slice();

  // Use two pointers to swap elements and reverse the list
  for (let i = 0, j = reversedList.length - 1; i < j; i++, j--) {
    const temp = reversedList[i];
    reversedList[i] = reversedList[j];
    reversedList[j] = temp;
  }

  return reversedList;
};
