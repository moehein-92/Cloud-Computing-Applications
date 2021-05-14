#!/usr/bin/env python3
import sys

lst = []

# input comes from STDIN
for line in sys.stdin:
    link, num_link = line.strip().split('\t')
    lst.append((link, int(num_link)))

lst = sorted(lst, key=lambda x: x[1])

for i in lst:
    print('%s\t%s' % (i[0], i[1])) #print as final output   