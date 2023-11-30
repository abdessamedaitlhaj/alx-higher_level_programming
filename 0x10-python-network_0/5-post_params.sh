#!/bin/bash
# sen POST request with variables
curl -s "$1" -X POST "email: test@gmail.com" "subject: I will always be here for PLD"
