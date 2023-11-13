#!/usr/bin/node
/* Script that prints the addition of 2 integers */

function add (a, b) {
  return (a + b);
}

const args = process.argv;
const n = parseInt(args[2]);
const m = parseInt(args[3]);
console.log(add(n, m));
