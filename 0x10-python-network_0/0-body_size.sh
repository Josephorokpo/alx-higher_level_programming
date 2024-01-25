#!/bin/bash
# displays the size of the response body in bytes in a URL using curl 

curl -s "$1" | wc -c
