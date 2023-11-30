#!/bin/bash
# Display the size of the body of the response
curl -Is "$1" | grep "Content-Length" | awk -F':' '{print $2}' | tr -d ' '
