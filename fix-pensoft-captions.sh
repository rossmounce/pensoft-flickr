#!/bin/bash
# Usage: correct caption files in all subfolders within the working directory

# Turning on the nullglob shell option
shopt -s nullglob

# Make list of all subfolders in working directory, save as pwd.txt
find * -maxdepth 0 -type d -exec bash -c "cd \"{}\"; pwd" \;  > pwd.txt

# Loop through pwd cd'ing into each directory then pdftotext all PDFs within each subdirectory
for i in $(cat pwd.txt); do
  cd $i
	echo "started on $i"
	find . -name "*.tmp" | xargs cat | tr -d '\n' | sed 's/\(Figure [0-9].\)/\n \1 /g' | sed 's/\(Figures [0-9].\)/\n \1 /g' | sed '/^\s*$/d' | sed '$a/END'  > captions.txt
	#sed -i '/^\s*$/d' captions.txt
	#sed -i '' -e '$a\' captions.txt 

done

