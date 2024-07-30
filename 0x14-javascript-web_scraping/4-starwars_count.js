#!/usr/bin/node

const request = require('request');

// Get the API URL from the first command line argument
const apiUrl = process.argv[2];

// Character ID for Wedge Antilles
const wedgeAntillesId = 18;

// Make a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response
  const data = JSON.parse(body);

  // Initialize the count of movies where Wedge Antilles appears
  let count = 0;

  // Iterate through each movie in the response
  data.results.forEach(movie => {
    // Check if Wedge Antilles is in the list of characters for the movie
    if (movie.characters.some(character => character.endsWith(`/${wedgeAntillesId}/`))) {
      count++;
    }
  });

  // Print the count of movies
  console.log(count);
});
