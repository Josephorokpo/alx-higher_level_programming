#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        # Handle exceptions and print the error message to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        return None
