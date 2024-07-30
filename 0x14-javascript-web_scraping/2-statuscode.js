#!/usr/bin/node

const request = require('request');

// Get the URL from the first command line argument
const url = process.argv[2];

// Perform a GET request to the URL
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  // Print the status code
  console.log(`code: ${response.statusCode}`);
});
