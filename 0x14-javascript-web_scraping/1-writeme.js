#!/usr/bin/node

const fs = require('fs');

// Gets the file path and string to write from command line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Checks if both arguments are provided
if (!filePath || !stringToWrite) {
  console.error('Usage: ./1-writeme.js <file_path> <string_to_write>');
  process.exit(1);
}

// Writes the string to the file in utf-8 encoding format
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    // Prints the error object if an error occurred during writing
    console.error(err);
  }
});
