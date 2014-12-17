'''
Created on Sep 25, 2014

@author: Cassie
'''

import re

text = ''.join(open('classbios.txt').readlines())
text2 = re.sub('([0-9][0-9]\s--*|--*)','', text)
sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text2)
for line in sentences:
    pattern1 = re.compile(r'\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?).*\s\d\d\d\d')
    pattern2 = re.compile("[Ii]n\s(19|20)\d\d")
    pattern3 = re.compile("(?:19|20)\d\d..s")   
    m = pattern1.search(line)
    n = pattern2.search(line)
    k = pattern3.search(line)
    if m is not None:
        if n is not None or m is not None:
            print line


