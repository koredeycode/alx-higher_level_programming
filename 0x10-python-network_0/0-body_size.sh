#!/bin/bash
#send a request to a url and display the size of response

url=$(curl -sL "$1")
echo ${#url}
