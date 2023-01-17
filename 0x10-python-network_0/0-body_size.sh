#!/bin/bash
#send a request to a url and display the size of response
curl -s "$1" | wc -c
