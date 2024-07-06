#!/usr/bin/python3
"""
A script that takes in a URL and an email address,
sends a POST request to the passed URL
with the email as a parameter, and displays the body of
the response.

Usage:
    ./6-post_email.py <URL> <email>
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the payload
    payload = {'email': email}

    # Send the POST request
    response = requests.post(url, data=payload)

    # Display the body of the response
    print(response.text)
