#!/bin/bash
# Display the body of HTTP response that has 200

http_code=$(curl -Is "$1" | grep "HTTP" | cut -d " " -f 2)
if [ "$http_code" -eq 200 ]; then
	curl "$1"
fi
