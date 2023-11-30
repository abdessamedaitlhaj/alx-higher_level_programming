#!/bin/bash
# send a request with a header variable

curl -sH "$1" "X-School-User-Id: 98"
