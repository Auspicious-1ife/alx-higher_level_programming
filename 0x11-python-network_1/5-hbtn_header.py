#!/usr/bin/python3
"""
This script takes in a URL, sends
a request to the URL, and
displays the value of the
X-Request-Id variable found in
the response header.
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