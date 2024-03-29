#!/usr/bin/python3
"""
Module: hbtn_status

This module fetches the status of https://alx-intranet.hbtn.io/status
and displays information about the response body.
"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
