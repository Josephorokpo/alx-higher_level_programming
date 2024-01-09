#!/usr/bin/node

const OldSquare = require('./5-square');

class Square extends OldSquare {
  constructor(size) {
    // Call the constructor of the parent class (OldSquare)
    super(size);
  }

  charPrint(c) {
    // If c is undefined, use the character X; otherwise, use the specified character
    const printChar = c || 'X';

    // Print the square using the specified character
    for (let i = 0; i < this.height; i++) {
      console.log(printChar.repeat(this.width));
    }
  }
}

module.exports = Square;
