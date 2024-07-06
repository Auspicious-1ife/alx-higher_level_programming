#!/usr/bin/python3
"""
This script fetches https://intranet.hbtn.io/status
using the requests package
and displays the body of the
response in the required format.
"""


import requests
# URL to fetch
url = "https://alx-intranet.hbtn.io/status"

# Make the request
response = requests.get(url)

# Get the content of the response
content = response.text


# Display the response in the required format
print("Body response:")
print("\t- type: {}".format(type(content)))
print("\t- content: {}".format(content))
