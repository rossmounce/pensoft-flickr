#!/bin/bash
docmd2="exiftool -h -charset utf8 -xmp:description='$3 $2'  $1"
eval "$docmd2"
