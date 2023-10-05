#!/usr/bin/python3

import sys


def main():
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 0:
        print("Number of argument(s): 0.")
        print(".")
    elif num_arguments == 1:
        print(f"Number of argument(s): 1.")
        print("1:", arguments[0])
    else:
        print(f"Number of arguments: {num_arguments}.")
        for i, arg in enumerate(arguments, start=1):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    main()
