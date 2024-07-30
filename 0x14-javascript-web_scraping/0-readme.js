#!/usr/bin/node

const fs = require('fs');

// Get the file path from the first command line argument
const filePath = process.argv[2];

// Read the file content in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // Print the error object if an error occurred during reading
    console.error(err);
  } else {
    // Print the content of the file
    console.log(data);
  }
});
