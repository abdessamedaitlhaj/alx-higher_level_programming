#!/bin/bash
# send POST request with variables
curl -s "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
