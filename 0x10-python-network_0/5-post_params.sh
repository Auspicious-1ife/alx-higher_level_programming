#!/bin/bash
# a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response, with a variable email and a variable subject
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
