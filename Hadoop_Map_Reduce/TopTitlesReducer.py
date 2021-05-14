#!/usr/bin/env python3
import sys


lst = []

# input comes from STDIN
for line in sys.stdin:
    word, count = line.strip().split('\t')
    lst.append((word, int(count)))

lst = sorted(lst, key=lambda x: x[1])

for i in lst:
    print('%s\t%s' % (i[0], i[1])) #print as final output            