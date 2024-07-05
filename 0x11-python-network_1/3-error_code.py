#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the body of the response
(decoded in utf-8). If an HTTPError occurs,
it prints the error code.
"""

import urllib.request
import urllib.error
import sys


def fetch_url(url):
    """Fetches the URL and prints the response body or the error code."""
    try:
        with urllib.request.urlopen(url) as response:
            response_body = response.read()
            print(response_body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
