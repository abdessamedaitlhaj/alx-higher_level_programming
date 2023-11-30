#!/bin/bash
# send a request with a header variable
curl -s "$1" -H "X-School-User-Id: 98"
