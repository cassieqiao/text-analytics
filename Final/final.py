'''
Created on Nov 29, 2014

@author: Cassie
'''
import whoosh
from whoosh.index import create_in
import os, os.path
from whoosh import index
from whoosh.fields import *
from os import listdir

schema = Schema(character_name =ID(stored=True), text=TEXT(stored=True))
if not os.path.exists("C:\Users\Cassie\Google Drive\MSiA\Fall 2014\MSiA 490\hw\index"):
    os.mkdir("C:\Users\Cassie\Google Drive\MSiA\Fall 2014\MSiA 490\hw\index")
ix = create_in("C:\Users\Cassie\Google Drive\MSiA\Fall 2014\MSiA 490\hw\index", schema)
writer = ix.writer()

for file in listdir("C:\Users\Cassie\Google Drive\MSiA\Fall 2014\MSiA 490\hw\characters"):
    path = 'C:\Users\Cassie\Google Drive\MSiA\Fall 2014\MSiA 490\hw\characters'
    filepath = path + '\\' + file
    with open (filepath, "r") as myfile:
        data=myfile.read().replace('\n', '')
        writer.add_document(character_name=unicode(file), text=unicode(data,errors='ignore'))
        
writer.commit()