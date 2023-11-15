#!/usr/bin/node
/* Add `width` and `height` atttributes to the class Rectangle */

class Rectangle {
  width;
  height;

  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
