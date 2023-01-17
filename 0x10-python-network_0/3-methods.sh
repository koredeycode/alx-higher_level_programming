#!/bin/bash
# displays the body of the response
curl -sI "$1" | grep "Allow" | cut -d " " -f 1-
