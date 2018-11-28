import whoosh
import os
from bs4 import BeautifulSoup
from bs4.element import Comment

import scrape
from whoosh.index import create_in
import urllib
from whoosh.index import open_dir
from whoosh.fields import Schema, ID, TEXT
from whoosh.qparser import QueryParser
from whoosh.query import *


if not os.path.exists("indexdir3"):
   os.mkdir("indexdir3")

schema =  Schema(link=ID(stored=True), content=TEXT)
ix = create_in("indexdir3", schema)


links=scrape.retSeeds()
cnt=0

for link in links:
   #if cnt <= 10:
      html = urllib.urlopen(link).read()
      soup = BeautifulSoup(html)
      [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
      content = soup.getText()
      writer = ix.writer()
      cnt+=1
      print "indexing doc:",cnt
      writer.add_document(link=link,content=content)
      writer.commit()
      ix = open_dir("indexdir3")










