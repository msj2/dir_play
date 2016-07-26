#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# I have 200+ html pages, which again have 15K+ resources in a single folder.
#I need to create directories (folders), see which resource is in which html file, move the relevant html file & it's resources 
#corresponding directories.
# Start with images, then move to all other static resources.
# Start by calling shell commands in a loop, but locate a way for the shell commands to be read from a text file/list...
#	Redirect stdin from text file/List ..?

import lxml.html
import string
from sys import argv
from datetime import datetime

#	have to use either of these, not both....
from subprocess import call
import os


#So many imports, need to cut this down !!!

path = "."	# Will this work?
detail_file = open('Detail_URL_file.txt','w')

#url = raw_input("Enter a website to extract the URL's from: ")
start = datetime.now()
image = lxml.html.parse(path)
image_list = image.xpath("//img/@src")	
a_list = image.xpath("//a/@href")	

os.system("mkdir 1")


for each in image_list:
	#print each
	line = "mv" + each + "1"
	call([line])
	

