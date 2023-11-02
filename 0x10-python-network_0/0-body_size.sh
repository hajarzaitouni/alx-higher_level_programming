#!/bin/bash
# displays the size of the body of the response using curl
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f2
