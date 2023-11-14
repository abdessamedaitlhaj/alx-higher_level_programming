#!/usr/bin/node
/* Function that executes x times a function */

exports.callMeBoy = function (x, theFun) {
  for (let i = 0; i < x; i++) {
    theFun();
  }
};
