'''
Created on Nov 4, 2014

@author: Cassie
'''
from nltk.classify import NaiveBayesClassifier
import urllib2
from bs4 import BeautifulSoup
import nltk
from nltk import ConfusionMatrix
import wikipedia

def word_feats(words):
    return dict([(word, True) for word in words.split() ])

asiaids = [u'detected',u'adds',u'exactly',u'difference',u'norwegian',u'benign',u'intend',u'perfectly',u'sounds',u'timely',
           u'trick',u'unusable',u'i.e',u'uzbekistan',u'nobody',u'realise',u'referencing',u'ang',u'b1',u'buying',u'chip',
           u'tajik',u'tashkent',u'complicated',u'terminology',u'definition',u'brunei', u'engagement',u'seal',u'contrasts']

africaids = [u'africa',u'ivory',u'contingent',u'egyptians',u'zaire',u'mine',u'saharan', u'mohamed', u'sahara',u'african',
             u'summer',u'1900s',u'970',u'abidjan',u'afternoons',u'algiers', u'bauxite',u'boma',u'cdg',u'diamonds',
             u'harmattan', u'miners',u'motorcycles',u'naba', u'namibian',u'oic',u'peuple', u'predecessors',u'shipment',
             u'nigeria' ]

europeids = [u'vienna', u'budapest',u'nazis',u'moscow',u'1923',u'1948',u'mikl\xf3s',u'anton',u'slovak',u'partisans',
            u'zagreb', u'riga',u'yugoslavia',u'prague',u'croatia',u'blum',u'frankfurt',u'jacobi',u'sevastopol',
            u'slavic',u'soviets',u'stepping',u'zur',u'critiques',u'emil',u'occupations',u'sergei',u'ussr',
            u'concentration',u'rudolf']

namerids= [u'caribbean',u'vote',u'afro',u'murders',u'grande',u'feet',u'panama',u'blacks',u'costa',u'modern', u'character',
           u'16.2',u'autobiography',u'molina',u'olive',u'payroll',u'prevailing',u'american',u'behavior',u'rica',u'linda',
            u'northeast',u'santo',u'santa',u'elimination',u'universidad',u'features',u'illegal',u'parks',u'los']

samerids = [u'alkaline',u'cbc',u'dynamical',u'femininity',u'foreword',u'graduating',u'kinetics',u'or\xe9al',u'phds',u'specialize',
           u'uni',u'zoology',u'colonizing',u'decimated',u'doctorates',u'examining',u'modelling', u'obstetrics',u'profession',
           u'prolific',u'avenida',u'arte',u'colegio',u'diario',u'jules',u'lecture',u'stirling',u'0.26',u'0371',u'0500291085']


oceniaids = [u'references',u'also',u'taro',u'was',u'which',u'see',u'first',u'links',u'has',u'polynesian',u'who',u'external',
             u'they',u'other',u'history',u'international',u'non',u'after',u'information',u'time',u'were',u'its',u'130\xbaw',
              u'170\xbae',u'40\xbas',u'accumulates',u'acidification',u'altimeters',u'aosis',u'aquifer']

antrcids = [u'saga',u'wwe',u'computation',u'fantastic',u'hannah',u'monkey',u'presenter',u'brad',u'carolyn',u'ronnie',
            u'schlesinger',u'anglican',u'collaborator',u'tone',u'1048', u'479',u'551',u'7pm',u'a.j',u'a.n',u'ablyazov',
            u'academi',u'accelerator',u'activate',u'actuary',u'adrienne',u'aenesidemus',u'africanist',u'agnostic',u'agnosticism']


asia_feats = [(word_feats(f), 'Asia') for f in asiaids ]
africa_feats = [(word_feats(f), 'Africa') for f in africaids ]
euro_feats = [(word_feats(f), 'Europe') for f in europeids ]
nameri_feats = [(word_feats(f), 'North America') for f in namerids ]
sameri_feats = [(word_feats(f), 'South America') for f in samerids ]
ocenia_feats = [(word_feats(f), 'Oceania') for f in oceniaids ]
antrc_feats = [(word_feats(f), 'Antarctica') for f in antrcids ]


trainfeats = asia_feats + africa_feats + euro_feats+nameri_feats+sameri_feats+ocenia_feats+antrc_feats
classi = NaiveBayesClassifier.train(trainfeats)

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
'''
chengdut =wikipedia.page("http://en.wikipedia.org/wiki/Chengdu").content 
pdist = classi.prob_classify(word_feats(chengdut))
print (pdist.prob('Asia'),  pdist.prob("Africa"), pdist.prob("North America"),
                        pdist.prob("South America"), pdist.prob("Europe"),pdist.prob("Oceania"),pdist.prob("Antarctica"))