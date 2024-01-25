#!/bin/bash
# displays the size of the response body in bytes in a URL using curl 

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request using curl in silent mode (-s) and get the size of the response body in bytes
response_size=$(curl -s -w "%{size_download}" -o /dev/null "$1")

# Display the size of the response body
echo "Size of the response body: $response_size bytes"
