#! /usr/bin/env python3

import os
from string import Template
from lxml import etree

def getTitle(lxmldom):
	for t in lxmldom.xpath("//title"):
		return t.text

def getContent(lxmldom):
	for c in lxmldom.xpath("//content"):
		return c.text

f = open('template')
template = f.read()
s = Template(template)

wwwdir = 'www/'

booksdir = 'books/'
listing = os.listdir(booksdir)
for book in listing:
	handle = open(booksdir + book)
	dom = etree.parse(handle)
	title = getTitle(dom)
	content = getContent(dom)
	bookHTML = s.safe_substitute(title=title, text=content)
	filename = book.replace('xml', 'html')
	savepath = wwwdir + filename
	try:
		print(bookHTML, file=wwwdir + filename)
	except:
		print("Error saving %(title)s to %(file)s" % {"title": title, "file": savepath})
	print("Saved %(title)s to %(filename)s" % {"title": title, "filename": filename})