#!/usr/bin/node
/* Function that executes x times a function */

module.exports = function (x, callMeMoby) {
  for (let i = 0; i < x; i++) {
    callMeMoby();
  }
});
