#!/usr/bin/python3
"""
Module: search_user

This module takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the letter from command line arguments or set it to an empty string if not provided
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # Send POST request to search_user endpoint with the letter as a parameter
    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})

    try:
        # Try to parse the response as JSON
        data = response.json()

        # Check if the JSON response is a list and not empty
        if isinstance(data, list) and data:
            # Display id and name for each user
            for user in data:
                print("[{}] {}".format(user.get('id'), user.get('name')))
