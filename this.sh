#!/usr/bin/env bash

for i in {0..9}
do
	a="0x0$i"
	a+="*"
	cd $a
	readme
	cd ..
done
