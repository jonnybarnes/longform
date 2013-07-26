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

dir = 'books/'
listing = os.listdir(dir)
for book in listing:
	handle = open(dir + book)
	dom = etree.parse(handle)
	title = getTitle(dom)
	content = getContent(dom)
	#print("Title: %s" % title)
	#print("Content: %s" % content)
	bookHTML = s.safe_substitute(title=title, text=content)
	print(bookHTML)