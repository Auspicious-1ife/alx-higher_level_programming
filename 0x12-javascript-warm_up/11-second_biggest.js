#!/usr/bin/node

// Retrieve the arguments from the command line (excluding the first two elements)
const args = process.argv.slice(2);

// Convert the arguments to integers
const nums = args.map(arg => parseInt(arg));

// Check the number of arguments
if (nums.length <= 1) {
  console.log(0);
} else {
  // Sort the numbers in descending order and find the second biggest
  nums.sort((a, b) => b - a);
  console.log(nums[1]);
}
