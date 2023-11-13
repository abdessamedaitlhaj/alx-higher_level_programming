#!/usr/bin/node
/* Script that prints the first argument passed to it */

const firstArg = process.argv[2];
if (firstArg) {
  console.log(firstArg);
}
