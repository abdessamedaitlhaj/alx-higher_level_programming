#!/usr/bin/node
/* Function that increments and calls a function */

exports.addMeMayBe = function (number, theFunction) {
  number++;
  theFunction(number);
};
