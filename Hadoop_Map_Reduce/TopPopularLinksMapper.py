#!/usr/bin/env python3
import sys

lst = []

for line in sys.stdin:
    link, num_link = line.split('\t')
    lst.append((link, int(num_link)))

lst = sorted(lst, key=lambda x: x[1])
lst = lst[-10:]

for i in lst:
    print('%s\t%s' % (i[0], i[1])) #pass this output to reducer