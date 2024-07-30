#!/usr/bin/node

const request = require('request');

// Get the API URL from the first command line argument
const apiUrl = process.argv[2];

// Make a GET request to the API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response
  const tasks = JSON.parse(body);

  // Create an object to count completed tasks by user ID
  const completedTasksCount = {};

  // Iterate through each task
  tasks.forEach(task => {
    if (task.completed) {
      // Increment the count for the user ID
      if (!completedTasksCount[task.userId]) {
        completedTasksCount[task.userId] = 0;
      }
      completedTasksCount[task.userId]++;
    }
  });

  // Print the completed tasks count for each user ID
  console.log(completedTasksCount);
});
