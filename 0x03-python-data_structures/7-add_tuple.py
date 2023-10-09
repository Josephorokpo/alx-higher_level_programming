#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples element-wise and return a new tuple."""
    # Extract the first two elements of each tuple (or use 0 if missing)
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0

    # Add the elements together and return a new tuple
    result_tuple = (a1 + b1, a2 + b2)
    return (result_tuple)
