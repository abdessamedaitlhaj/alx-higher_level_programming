#!/usr/bin/node
/* Add `rotate` and `double` methods  */
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

  rotate () {
    const tmpWidth = this.width;
    this.width = this.height;
    this.height = tmpWidth;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
