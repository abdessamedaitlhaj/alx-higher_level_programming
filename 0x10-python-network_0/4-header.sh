#!/bin/bash
# Send a GET request to the URL with a header variable and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
