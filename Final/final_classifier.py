'''
Created on Nov 4, 2014

@author: Cassie
'''
from nltk.classify import NaiveBayesClassifier
import urllib2
from bs4 import BeautifulSoup
import nltk
from nltk import ConfusionMatrix
from os import listdir


def word_feats(words):
    return dict([(word, True) for word in words.split() ])

clovids = [u'above',u'absorbed',u'act',u'adjusts', u'admiringly',u'age', u'ago', u'alacrity', u'anywhere', 
u'applies', u'approaches', u'attention', u'bearing', u'beast', u'beauty', u'becomes', u'best', u'between', 
u'bicycles', u'bled', u'bonnyonce', u'boots', u'briskly', u'burying', u'catheter', u'cell', u'changes', 
u'christ',u'climbed', u'coffins']

hammids = [u'aah',u'abandon', u'absent', u'absently', u'accepting', u'accursed',u'afraid', u'ages',
u'agitated', u'agree', u'air', u'alive',u'alivea', u'alone',u'already', u'among', u'anenometer', 
u'anger',u'animated', u'anxious', u'ape',u'aperture',u'apologies',u'appalled', u'appears',u'ardour',
u'aren', u'armrests', u'arms', u'arses']

monoids = [u'armchair', u'ashbins', u'ashbins.center', u'bare', u'blood', u'covered', u'covering', 
u'curtains', u'drawn.front', u'draws', u'face.brief', u'hamm.motionless', u'hanging', u'interior.grey', 
u'large', u'light.left', u'picture.front', u'socks',u'staggering', u'stained', u'tableau.clov', u'thick', 
u'touching', u'windows',u'arm', u'castors',u'curtain', u'dressing', u'example', u'folds']

naggids= [u'art', u'ballockses', u'balls', u'blowing', u'bluebells', u'breaks',u'buttonholes',u'capable', 
u'capsized', u'cautiously', u'changed', u'cheer', u'chuckles', u'clasping', u'closing', u'crashed', u'crotch', 
u'customer', u'dear', u'delight', u'disdainful',u'disgustedly', u'dreadfully', u'drowned', u'earshot', 
u'englishman',u'excuse', u'fail',u'failed', u'fetches']

nellids = [u'accurate', u'afternoon', u'april', u'ardennes', u'bottom',u'clean', u'como', u'elegiac', 
u'felt', u'funnier', u'lake',u'most', u'mustn', u'often', u'perished',u'pet',u'quite', u'rowing', u'rub', 
u'unhappiness', u'warily', u'because', u'beginning',u'comical', u'deep', u'desert', u'engaged', u'farce', 
u'funny', u'grant']


clov_feats = [(word_feats(f), 'Clov') for f in clovids ]
hamm_feats = [(word_feats(f), 'Hamm') for f in hammids ]
mono_feats = [(word_feats(f), 'Monologue') for f in monoids ]
nagg_feats = [(word_feats(f), 'Nagg') for f in naggids ]
nell_feats = [(word_feats(f), 'Nell') for f in nellids ]

trainfeats = clov_feats + hamm_feats + mono_feats+nagg_feats+nell_feats
classi = NaiveBayesClassifier.train(trainfeats)
files = ["Clov","Hamm","Monologue","Nagg","Nell"]
ref = ""
tagged = ""
index = 0

for file in listdir("C:\Users\Cassie\Google Drive\MSiA\Fall 2014\MSiA 490\hw\characters"):
    path = 'C:\Users\Cassie\Google Drive\MSiA\Fall 2014\MSiA 490\hw\characters'
    filepath = path + '\\' + file
    with open (filepath, "r") as myfile:
        index +=1
        for line in myfile:
            ref = ref + ',' + files[index-1]
            tag = classi.classify(word_feats(line))
            tagged = tagged + ',' + tag

print ConfusionMatrix(ref.split(',')[1:], tagged.split(',')[1:])
             
'''
soup = BeautifulSoup(open("wiki.html"))
tables = soup.findAll("table", { "class" : "wikitable sortable" })
ref = ""
tagged = ""
continents = ["Africa","Asia","Europe","North America","South America","Oceania","Antrctica"]
index = 0
for table in tables:
    index +=1
    for row in table.findAll('tr'):
        cells = row.findAll("td")
        if len(cells) == 5:       
            if cells[2].find('a',text=True) is not None:
                b = cells[2].find('a',text=True)
                cityname = b['title']
                citylink = 'http://en.wikipedia.org'+b['href']
                try:
                    cityt = wikipedia.page(citylink).content 
                except:
                    cityt = None
            else:
                cityname = u"Null"
                cityt = None
            
            if cityt is not None:     
                ref = ref + ',' + continents[index-1]
                tag = classi.classify(word_feats(cityt))
                tagged = tagged + ',' + tag
                 
print ConfusionMatrix(ref.split(','), tagged.split(','))

chengdut =wikipedia.page("http://en.wikipedia.org/wiki/Chengdu").content 
pdist = classi.prob_classify(word_feats(chengdut))
print (pdist.prob('Asia'),  pdist.prob("Africa"), pdist.prob("North America"),
                        pdist.prob("South America"), pdist.prob("Europe"),pdist.prob("Oceania"),pdist.prob("Antarctica"))
'''