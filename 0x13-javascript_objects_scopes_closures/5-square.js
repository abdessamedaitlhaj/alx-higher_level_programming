#!/usr/bin/node
/* Class Square that defines a square and inherits from Rectangle */

const Rectangle = require('./4-rectangle.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;