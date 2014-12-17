'''
Created on Oct 27, 2014

@author: Cassie
'''

import urllib2
from bs4 import BeautifulSoup
import whoosh
from whoosh.index import create_in
import os, os.path
from whoosh import index
from whoosh.fields import *


schema = Schema(country_name =ID(stored=True), country_text=TEXT, continent=ID(stored=True), city_name=ID(stored=True),city_text =TEXT(stored=True))
if not os.path.exists("index"):
    os.mkdir("index")
ix = create_in("index", schema)
writer = ix.writer()


soup = BeautifulSoup(open("wiki.html"))

tables = soup.findAll("table", { "class" : "wikitable sortable" })
continents = ["Africa","Asia","Europe","North America","South America","Oceania","Antrctica"]
index = 0

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    elif re.match('\n',str(element)):
        return False
    else:
        return True

for table in tables:
    index +=1
    for row in table.findAll('tr'):
        cells = row.findAll("td")
        if len(cells) == 5:
            a = cells[1].find('a',text=True)
            countryname = a['title']
            countrylink = 'http://en.wikipedia.org'+a['href'] 
            countryhtml = urllib2.urlopen(countrylink).read()
            countrysoup = BeautifulSoup(countryhtml)
            countrytexts = countrysoup.findAll(text=True)
            countrytext = filter(visible, countrytexts)
            countryt =   ''.join(countrytext)       
            if cells[2].find('a',text=True) is not None:
                b = cells[2].find('a',text=True)
                cityname = b['title']
                citylink = 'http://en.wikipedia.org'+b['href']
                cityhtml = urllib2.urlopen(citylink).read()
                citysoup = BeautifulSoup(cityhtml)
                citytexts = citysoup.findAll(text=True)
                citytext = filter(visible, citytexts)
                cityt = ''.join(citytext)  
            else:
                cityname = u"Null"
                cityt = None  
            writer.add_document(country_name=countryname, country_text =countryt,
                continent=unicode(continents[index-1]),city_name=cityname,city_text=cityt)

writer.commit()
