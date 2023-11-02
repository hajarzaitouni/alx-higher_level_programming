#!/bin/bash
# sends a JSON POST request to a URL with json File as argument
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
