#!/bin/bash
# Send a DELETE request to the URL passed as the first argument and displays the body of the response
curl curl -sX DELETE "$1"
