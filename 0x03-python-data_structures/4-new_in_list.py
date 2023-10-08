#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""

    # Check for invalid input
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()

    # Create a copy of the original list
    new_list = my_list.copy()

    # Replace the element at the specified index
    new_list[idx] = element

    return (new_list)
