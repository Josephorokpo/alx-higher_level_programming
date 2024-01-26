#!/usr/bin/python3
"""
Module: hbtn_status

This module fetches https://alx-intranet.hbtn.io/status using the requests package
and displays information about the response body.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
