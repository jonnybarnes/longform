#! /usr/bin/env python3

import os
from string import Template
from lxml import etree

wwwdir = 'www/'
booksdir = 'books/'

def getTitle(lxmldom):
	for t in lxmldom.xpath("//title"):
		return t.text

def getContent(lxmldom):
	for c in lxmldom.xpath("//content"):
		return c.text

f = open('template')
template = f.read()
s = Template(template)

listing = os.listdir(booksdir)
for book in listing:
	handle = open(booksdir + book)
	dom = etree.parse(handle)
	title = getTitle(dom)
	content = getContent(dom)
	bookHTML = s.safe_substitute(title=title, content=content)
	filename = book.replace('xml', 'html')
	savepath = wwwdir + filename
	try:
		writer = open(wwwdir + filename, 'w')
		writer.write(bookHTML)
		writer.close()
		print("Saved %(title)s to %(filename)s" % {"title": title, "filename": filename})
	except:
		print("Error saving %(title)s to %(file)s" % {"title": title, "file": savepath})