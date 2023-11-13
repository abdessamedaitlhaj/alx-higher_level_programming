#!/usr/bin/node
/* Script that searches the second biggest integer in the list of arguments */

const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  const myList = [];
  for (let i = 2; i < args.length; i++) {
    myList.push(parseInt(args[i]));
  }
  myList.sort((a, b) => b - a);
  console.log(myList[1]);
}
