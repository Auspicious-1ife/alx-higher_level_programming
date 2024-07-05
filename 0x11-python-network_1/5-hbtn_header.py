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


def fetch_request_id(url):
    """Fetches the value of
    X-Request-Id from the
    response header."""
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')

    if request_id:
        print(request_id)
    else:
        print("No X-Request-Id found in the response headers.")


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_request_id(url)
