#!/bin/bash

# Send a POST request to the passed URL with variables, and displays the body of the response

curl -s "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
