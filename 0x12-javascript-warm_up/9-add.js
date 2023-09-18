#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const args = process.argv;
const myInt1 = parseInt(args[2]);
const myInt2 = parseInt(args[3]);
if (isNaN(myInt1) || isNaN(myInt2)) console.log('NaN');
else console.log(add(myInt1, myInt2));
