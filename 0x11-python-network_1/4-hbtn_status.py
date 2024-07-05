#!/usr/bin/python3
"""
This script fetches https://intranet.hbtn.io/status
using the requests package
and displays the body of the
response in the required format.
"""

import requests


def fetch_status():
    """Fetches and displays the status from https://intranet.hbtn.io/status."""
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)
    content = response.text.strip()

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))


if __name__ == "__main__":
    fetch_status()
