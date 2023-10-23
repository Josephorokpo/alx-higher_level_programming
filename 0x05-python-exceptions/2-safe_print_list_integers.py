#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_elements = 0
    for i in range(0, x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end=' ')
                printed_elements += 1
        except (ValueError, TypeError):
            continue
    print()
    return (printed_elements)
