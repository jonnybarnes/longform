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

def getAuthor(lxmldom):
	for a in lxmldom.xpath("//author"):
		return a.text

def getCategory(lxmldom):
	for cat in lxmldom.xpath("//category"):
		return cat.text

ft = open('template')
template = ft.read()
s = Template(template)

"""Create the books and populate the index variables"""
fiction = dict()
nonfiction = dict()
listing = os.listdir(booksdir)
for book in listing:
	handle = open(booksdir + book)
	dom = etree.parse(handle)
	title = getTitle(dom)
	content = getContent(dom)
	author = getAuthor(dom)
	category = getCategory(dom)
	bookHTML = s.safe_substitute(title=title, content=content)
	filename = book.replace('xml', 'html')
	if(category == 'fiction'):
		fiction[filename] = title
	else:
		nonfiction[filename] = title
	savepath = wwwdir + filename
	try:
		writer = open(wwwdir + filename, 'w')
		writer.write(bookHTML)
		writer.close()
		print("Saved %(title)s to %(filename)s" % {"title": title, "filename": filename})
	except:
		print("Error saving %(title)s to %(file)s" % {"title": title, "file": savepath})

indexTitle = 'A Good Long Read'
fictionLinks = ''
nonfictionLinks = ''
for key, value in fiction.items():
    fictionLinks = fictionLinks + '<li><a href="' + key  + '">' + value + '</a></li>'
for key, value in nonfiction.items():
    fictionLinks += '<li><a href="' + key  + '">' + value + '</a></li>'
indexContemt = """<header>
    <h1>A GOOD LONG READ</h1>
  </header>

  <h2>Welcome</h2>
  <p>The aim of this little project is to present some popular literrary works through the browser. Hopefully these are easy and pleasurable to read wether on your desktop or your mobile.</p>

  <h2>The Works</h2>
  <nav id="works">
    <h3>Fiction</h3>
    <ul>""" + fictionLinks + """
    </ul>
    <h3>Non-Fiction</h3>
    <ul>""" + nonfictionLinks + """</ul>
  </nav>

  <h2>Colophon</h2>
  <p>This site is presented in Adobe Garamond Pro served by <a href="https://typekit.com/">Typekit</a>, the typography is aided by <a href="http://typeplate.com/">Typeplate</a>. The text for the books are provided by the <a href="http://www.gutenberg.org/">Gutenberg Project</a>. You can get in touch with me vie <a href="https://twitter.com/jonnybarnes">Twitter</a>, <a href="https://alpha.app.net/jonnybarnes">App.net</a>, or <a href="mailto:jonny@jonnybarnes.net">e-mail</a>.</p>"""

indexHTML = s.safe_substitute(title=indexTitle, content=indexContemt)
try:
	writer = open(wwwdir + 'index.html', 'w')
	writer.write(indexHTML)
	writer.close()
	print('Saved index.html')
except:
	print('Error saving index.html')