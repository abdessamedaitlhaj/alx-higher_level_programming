#!/usr/bin/node
/* Script that computes and prints a factorial */

function factorial(n) {
  if (n <= 1) {
    return (1);
  }
  else {
    return (n * factorial(n - 1));
  }
}

const args = process.argv;
const n = parseInt(args[2]);
if (isNaN(n)) {
  console.log(1);
} else {
  console.log(factorial(n));
}
