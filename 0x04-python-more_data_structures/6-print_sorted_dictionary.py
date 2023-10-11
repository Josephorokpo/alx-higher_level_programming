#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """A function that prints a dictionary by ordered keys."""
    for key in sorted(a_dictionary.keys()):
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
