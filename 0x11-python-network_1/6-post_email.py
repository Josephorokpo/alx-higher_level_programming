#!/usr/bin/python3
"""
Module: post_email

This module takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Send POST request with email parameter
    response = requests.post(url, data={'email': email})

    # Display the body of the response
    print(response.text)
