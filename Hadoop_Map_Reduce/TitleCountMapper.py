#!/usr/bin/env python3

import sys
import string

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

with open(stopWordsPath) as f:
    stopList = f.read().splitlines()

with open(delimitersPath) as f:
    delims = list(f.read())

for line in sys.stdin:
    line = line.strip().lower()
    for i in delims:
        line = line.replace(i, " ") 
        words = line.split() 
    words = [i for i in words if i not in stopList]
    for word in words:
        print('%s\t%s' % (word, 1)) #pass this output to reducer
