#!/usr/bin/node
/* Function that increments and calls a function */

module.exports = function (number, addMeBoy) {
  number++;
  addMeBoy(number);
});
