#!/usr/bin/node
/* Function that converts a number from base 10 to another base passed as argument */

exports.converter = function (base) {
  while (base / 10) {
    console.log(base % 10);
    base /= 10;
  }
};
