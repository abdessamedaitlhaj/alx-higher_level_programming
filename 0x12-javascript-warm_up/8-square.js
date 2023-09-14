#!/usr/bin/node
const args = process.argv;
if (args.length <= 2) {
  console.log('Missing size');
} else {
  const myInt = parseInt(args[2]);
  if (myInt > 0) {
    let row = '';
    for (let i = 0; i < myInt; i++) {
      row = '';
      for (let j = 0; j < myInt; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
