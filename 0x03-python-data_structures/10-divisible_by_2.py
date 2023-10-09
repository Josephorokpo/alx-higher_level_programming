#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list."""

    # Initialize an empty list to store results
    new_list = []
    for num in my_list:
        
        # Use '==' for equality comparison
        if num % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    # Return the list of True/False values
    return (new_list)
