#!/bin/bash

# Get http header length

curl -s "$1" | wc -c
