#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys
import getopt 
import os
import re
import string

soup = BeautifulSoup (open(sys.argv[1]))

dirname = sys.argv[1]
chomped = dirname[:-5]
strang = re.sub('[^0-9]', '', dirname[:-14])
#print string
#print dirname
print chomped

#text captions

figcap = soup.find_all('div', class_="ImgTextFloatRight")
#print(figcap)

file = open("./"+chomped+"/"+chomped+".tmp", "wb")

for tr in figcap[1::2]:
        cap = (tr.get_text()).strip().encode("utf8")
        #print cap
        file.write(cap+'\n')

file.flush()
file.close()

#image links

figimg = soup.find_all('div', class_="graphicImg")
#print(figimg)

file = open("./"+chomped+"/"+chomped+"-imgs.txt", "wb")

strang = re.sub('[^0-9]', '', dirname[:-14])
for tr in figimg[1::2]:
    imgs = tr.find('a')['href']
    #print ("http://www.pensoft.net/J_FILES/1/articles/"+strang+"/"+imgs)
    file.write("http://www.pensoft.net/J_FILES/1/articles/"+strang+"/"+imgs+'\n')

file.flush()
file.close()

# BIBINFO

ayt = soup.find_all('div', class_="authors")
#print (ayt)

tit = soup.find('title').encode("utf8")
title = tit.replace("<title>","").replace("</title>","")
doibit = soup.find('div', class_="doiNumber")
outit = (doibit.string).strip().replace("doi: ","http://dx.doi.org/").encode("utf8","ignore")
blah = outit.strip().replace("doi: ","http://dx.doi.org/")

file = open("./"+chomped+"/bibinfo.txt", "wb")


#print (title+". "+outit)
#file.write(title+". "+outit)
from string import digits
for bl in ayt:
        authors = (bl.get_text()).encode("utf8","ignore")
        cheese = (authors.translate(None, digits)).replace("†","").replace("‡","").replace("§","").replace("|","").replace("¶","").replace("#","").replace(",,",",")
	final = cheese.decode('utf8','ignore')
        #print (re.sub('[\W_]+', ' ', authors)) #Carmelo And jar1 Carles Hernando2 Ignacio Ribera3 
        #print (cheese+" "+title+". "+outit)
        file.write("Source: "+(final.encode("utf8"))+" "+title+". "+outit)

file.flush()
file.close()
