'''
Created on Oct 30, 2014

@author: Cassie
'''
from whoosh import index
from whoosh.qparser import QueryParser
from whoosh.query import And, Term, Not, FuzzyTerm, Phrase
import math
from operator import itemgetter
from nltk.classify import NaiveBayesClassifier

ix = index.open_dir("C:\Users\Cassie\Google Drive\MSiA\Fall 2014\MSiA 490\hw\index")
reader = ix.reader()

#extract dictionary
unique_words = reader.field_terms('text')
continents = [u"Africa",u"Asia",u"Europe",u"North America",u"South America",u"Oceania",u"Antrctica"]


def mutual_information(word,tag):
    # n11 is the number of posts where tag and term occur together
    N_1_1 = 1.0
    # n10 is the number of posts where tag doesn't occur and term does
    N_1_0 = 0.0
    #total number of docs for tag
    total_tag_doc_count = 59.0
    #total number of docs
    total_docs = 268.0
    
    q= Term("text",word)
    with ix.searcher() as s:
        results = s.search(q,limit=None)
        for a in results:
            if a['character_name']==tag:
                N_1_1+=1.0
            else:
                N_1_0+=1.0
    
        
    # n01 is the number of posts where tag occurs and term doesn't
    N_0_1 = total_tag_doc_count+1 - N_1_1
    

    # n00 is the number of posts where tag doesn't occur and term doesn't
    N_0_0 = total_docs - N_1_1 - N_1_0 - N_0_1

    N_1_A = N_1_1 + N_1_0  # N_1_A is the number of posts that contain the token    
    N_A_1 = N_1_1 + N_0_1 
    N_0_A = N_0_1 + N_0_0
    N_A_0 = N_0_0 + N_1_0 # N_0_A is the number of posts that don't contain the token
    
    if N_1_A == 0 or N_A_1 == 0 or N_0_A == 0 or N_A_0 == 0:
        return 0
    

    part1 = (N_1_1 / total_docs) * math.log((total_docs * N_1_1) / (N_1_A * N_A_1), 2)
  
    if N_0_1 == 0:
        part2 = 0
    else:
        part2 = (N_0_1 / total_docs) * math.log((total_docs * N_0_1) / (N_0_A * N_A_1), 2)
    
    if N_1_0 == 0:
        part3 = 0
    else:
        part3 = (N_1_0 / total_docs) * math.log((total_docs * N_1_0) / (N_1_A * N_A_0), 2)

    if N_0_0 == 0:
        part4 = 0
    else:
        part4 = (N_0_0 / total_docs) * math.log((total_docs * N_0_0) / (N_A_0 * N_0_A), 2)

    mi_score = part1 + part2 + part3 + part4
    
    return mi_score

textterms_scores = []

for word in unique_words:
    mi_score = mutual_information(word,u"nell.txt")
    entry = (word, "nell.txt", [round(mi_score * 10000, 6)])
    textterms_scores.append(entry)

top30_textterms = sorted(textterms_scores, key=itemgetter(2), reverse=True)[:30]
#unique_terms = set(word_list)
for a in top30_textterms:
    print a
#classi = NaiveBayesClassifier.train(features)
