#!/usr/bin/python3
"""
This module provides functionality to fetch and display the status from a URL.
"""

import urllib.request


def fetch_status(url):
    """Fetches and prints the status from the specified URL."""
    with urllib.request.urlopen(url) as response:
        body = response.read()
        decoded_body = body.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(decoded_body))

    if __name__ == "__main__":
        url = 'https://alx-intranet.hbtn.io/status'
    fetch_status(url)
