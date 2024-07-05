#!/bin/bash
# A bash script that takes in a uRL asnd sends a request to that URL and displays the body size of the response
curl -s "$1" | wc -c
