#!/usr/bin/node
/* Script that prints x times “C is fun” */

const args = process.argv;
if (args.length <= 2) {
  console.log('Missing number of occurrences');
} else {
  const x = args[2];
  if (x > 0) {
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  }
}
