#!/usr/bin/node

const request = require('request');

// Get the movie ID from the first command line argument
const movieId = process.argv[2];

// Construct the URL for the Star Wars API endpoint for the movie
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API for the movie
request.get(movieUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response
  const movie = JSON.parse(body);

  // Get the list of character URLs
  const characterUrls = movie.characters;

  // Function to fetch and print character names
  const printCharacterNames = (urls, index = 0) => {
    if (index >= urls.length) {
      return;
    }

    // Make a GET request to the URL for the current character
    request.get(urls[index], (err, res, body) => {
      if (err) {
        console.error(err);
        return;
      }

      // Parse the JSON response and print the character name
      const character = JSON.parse(body);
      console.log(character.name);

      // Recursively fetch the next character
      printCharacterNames(urls, index + 1);
    });
  };

  // Start fetching character names
  printCharacterNames(characterUrls);
});
