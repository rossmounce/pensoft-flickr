pensoft-flickr
==============

An adaption of my workflow for BMC journals, which is posted at: https://github.com/rossmounce/Trying-beautiful-soup 

Developed in bash & python with Beautiful Soup.


# Get full-text HTML articles from ZooKeys that contain phylogenies

wget -w 30 -i layout.txt

mmv "*.htm" "#1.html"   # There is much inconsistency between articles as to the URL extension. Sometimes 'html' sometimes 'htm'



# Running it

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


