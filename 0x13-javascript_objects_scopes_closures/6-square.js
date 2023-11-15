#!/usr/bin/node
/*
`charPrint` that prints the rectangle using
the character c, if it is undefined the char 'X' will be used
*/

const OldSquare = require('./5-square.js');
class Square extends OldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      let X = '';
      for (let i = 0; i < this.width; i++) {
        for (let j = 0; j < this.height; j++) {
          X += c;
        }
        console.log(X);
        X = '';
      }
    } else {
        this.print();
      }
  }
}
module.exports = Square;
