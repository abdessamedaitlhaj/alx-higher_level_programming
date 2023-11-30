#!/bin/bash
# list all methods within an HTPP response

curl -sI "$1" | grep "Allow" | awk '{print $2}'
