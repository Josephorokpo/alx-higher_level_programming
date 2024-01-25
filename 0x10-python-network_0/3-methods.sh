#!/bin/bash
# This script takes a URL as input and shows all HTTP methods accepted by the server
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
