#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the
passed URL with the email
as a parameter, and displays the
body of the response
(decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys


def send_post_request(url, email):
    """Sends a POST request to the specified URL
    with the email as a parameter and prints the response."""
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        response_body = response.read()
        print(response_body.decode('utf-8'))


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
