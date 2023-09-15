#!/usr/bin/node

const numbers = process.argv;
if (numbers.length <= 3) console.log(0);
else {
  const arr = [];
  for (let i = 2; i < numbers.length; i++) {
    arr[i - 2] = parseInt(numbers[i]);
  }
  arr.sort((a, b) => a - b);
  console.log(arr[arr.length - 2]);
}
