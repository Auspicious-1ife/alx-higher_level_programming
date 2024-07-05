#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the value of the
X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys


def fetch_x_request_id(url):
    """Fetches and prints the value of the X-Request-Id
    from the specified URL."""
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
    print(x_request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_x_request_id(url)
