#!/usr/bin/node

const request = require('request');

// Get the movie ID from the first command line argument
const movieId = process.argv[2];

// Construct the URL for the Star Wars API endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response
  const data = JSON.parse(body);

  // Print the title of the movie
  console.log(data.title);
});
