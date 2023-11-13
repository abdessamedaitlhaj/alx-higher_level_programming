#!/usr/bin/node
/* Script that prints a square */

const args = process.argv;
const n = parseInt(args[2]);
if (isNaN(n) || args.length <= 2) {
  console.log('Missing size');
} else {
  let X;
  for (let i = 0; i < n; i++) {
    X = '';
    for (let j = 0; j < n; j++) {
      X += 'X';
    }
    console.log(X);
  }
}
