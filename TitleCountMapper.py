#!/usr/bin/env python3

import sys
import string

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

with open(stopWordsPath) as f:
    stopWords = set(word.strip() for word in f)

with open(delimitersPath) as f:
    delimiters = f.read().strip()
        
for line in sys.stdin:
    for delimiter in delimiters:
        line = line.replace(delimiter, ' ').lower()
    tokens = line.split()
    
    tokens = [token for token in tokens if token not in stopWords]

    for token in tokens:
        print('%s\t%s' % (token, 1))