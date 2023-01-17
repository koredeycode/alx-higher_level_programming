#!/bin/bash
# send a post request to the pass url
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
