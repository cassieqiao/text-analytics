'''
Created on Oct 27, 2014

@author: Cassie
'''
from whoosh import index
from whoosh.qparser import QueryParser
from whoosh.query import And, Term, Not, FuzzyTerm, Phrase

ix = index.open_dir("index")


q1 = And([Term("city_text", u"greek"),
      Term("city_text", u"roman"),
      Not(Term("city_text", u"persian"))])
q2 = FuzzyTerm("city_text", u"shakespeare")
q3= Phrase("city_text", [u"located",u"below", u"sea", u"level"], slop=10)

with ix.searcher() as s:
    results = s.search(q2,limit=None)
    for a in results:
        print a['city_name']


    