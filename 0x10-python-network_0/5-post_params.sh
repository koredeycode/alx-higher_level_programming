#!/bin/bash
# send a post request to the pass url
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
