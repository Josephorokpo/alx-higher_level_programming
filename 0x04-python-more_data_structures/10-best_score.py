#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not a_dictionary:
        return None

    max_score = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value == max_score:
            return key

    return None
