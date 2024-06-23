#!/usr/bin/node
// Function to add two integers
function add (a, b) {
  return a + b;
}
const arg1 = process.argv[2];
const arg2 = process.argv[3];
const int1 = parseInt(arg1);
const int2 = parseInt(arg2);
if (isNaN(int1) || isNaN(int2)) {
  console.log('NaN');
} else {
  console.log(add(int1, int2));
}
