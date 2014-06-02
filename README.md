pensoft-flickr
==============

An adaption of my workflow for BMC journals, which is posted at: https://github.com/rossmounce/Trying-beautiful-soup 

Developed in bash & python with Beautiful Soup.

# Running it

* Run bash create_subfolders.sh first to create a subfolder for each html file (I would do this in the python script if I knew how!)
* Iterate over each html file, applying the beautiful soup python script to each:
```
bash html_create_subfolders.sh ; #creates a subfolder for each fulltext html article
for i in *.html ; do python pensoft-get-figures.py $i ; done ;   #extracts the figure image links, bibliographic data and figure caption text
bash download-figs.sh ;
bash remove-apos.sh ; #Removes all apostrophes from all caption plaintext files
bash fix-pensoft-captions.sh; #ensures that each figure caption takes up just one (long) line
bash exif-CCBY-Pensoft.sh ; #embeds constant strings : BioMed Central & CC BY 
bash embedxmp.sh ; # this script calls on "doexif.sh" so make sure it's executable
```

bash create_subfolders can be happily re-run without losing what has been done in the next two lines


