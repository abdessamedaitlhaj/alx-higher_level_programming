#!/bin/bash
# list all methods within an HTPP response
curl -sI "$1" | grep "Allowed" | awk -F ":" '{print $2}' | tr -d " "
