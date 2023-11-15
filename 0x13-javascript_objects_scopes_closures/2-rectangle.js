#!/usr/bin/node
/* If w or h is equal to 0 or not a positive integer, an empty object will be created */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
