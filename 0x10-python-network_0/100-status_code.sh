#!/bin/bash
# send a post request to the pass url
curl -sL -w "%{http_code}" -o /dev/null "$1"
