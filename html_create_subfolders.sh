#!/bin/bash
for f in *.html
	do
	echo "started on $f"
	STEM=$(echo $f | sed 's/.....$//g' )
	mkdir $STEM
	done
