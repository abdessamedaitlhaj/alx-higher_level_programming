#!/usr/bin/node
const args = process.argv
const myInt = parseInt(args[2]);
if (!isNaN(myInt)) console.log('My number: ' + myInt);
else console.log('Not a number');
