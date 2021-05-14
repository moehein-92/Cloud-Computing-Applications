#!/usr/bin/env python3

from operator import itemgetter
import sys

dic = {}

# input comes from STDIN
for line in sys.stdin:
    word, count = line.split('\t', 1)
    if word in dic:
        dic[word] += int(count)
    else:
        dic[word] = int(count)
    
for key in dic:
    #if dic[key] > 1:
    print('%s\t%s' % (key, dic[key])) #print as final output
                                   