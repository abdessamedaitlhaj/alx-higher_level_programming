#!/usr/bin/node
/* Add `print` to print a rectangle shape using `width` & `height` of the class Rectangle */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let X = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        X += 'X';
      }
      console.log(X);
      X = '';
    }
  }
}
module.exports = Rectangle;
