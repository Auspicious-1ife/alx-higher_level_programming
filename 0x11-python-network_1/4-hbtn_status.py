#!/usr/bin/python3i
"""
This script fetches https://alx-intranet.hbtn.io/status
using the requests package
and displays the body of the
response in the required format.
"""

import requests


def fetch_status():
    """Fetches and displays the
    status from https://alx-intranet.hbtn.io/status."""
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    data = response.json()  # Assuming the response content is JSON

    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))


if __name__ == "__main__":
    fetch_status()
