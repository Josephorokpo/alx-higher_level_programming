#!/bin/bash
# This script sends a request to a URL passed as an argument and displays only the status code of the response.
awk 'NR==1{printf "%s", $2}' response_headers.txt $(curl -sI "$1" -o response_headers.txt)
