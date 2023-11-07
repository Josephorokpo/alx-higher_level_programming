#!/usr/bin/python3
"""
A a script that reads stdin line by line and computes metrics.
"""


import sys
import signal


# Define signal handler for CTRL+C
def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Initialize variables to store metrics
total_file_size = 0
status_codes = {}


# Function to print metrics
def print_metrics():
    print(f"Total file size: {total_file_size} bytes")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


line_count = 0

# Read input line by line from stdin
for line in sys.stdin:
    line_count += 1
    parts = line.split()
    if len(parts) > 8:
        status_code = parts[-2]
        file_size = int(parts[-1])
        total_file_size += file_size

        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1
    if line_count % 10 == 0:
        print_metrics()
