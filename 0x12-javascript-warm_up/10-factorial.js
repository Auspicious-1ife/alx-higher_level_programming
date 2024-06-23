#!/usr/bin/node

// Recursive function to compute factorial
function factorial (n) {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

// Retrieve the argument from the command line
const arg = process.argv[2];

// Attempt to convert the argument to an integer
const number = parseInt(arg);

// Compute the factorial, treating NaN as 1
const result = isNaN(number) ? 1 : factorial(number);

// Print the result
console.log(result);
