#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const args = process.argv;
if (args.length <= 3) {
  console.log('NaN');
} else {
  const myInt1 = parseInt(args[2]);
  const myInt2 = parseInt(args[3]);
  if (isNaN(myInt1) || isNaN(myInt2)) console.log('NaN');
  else console.log(add(args[2], args[3]));
}
