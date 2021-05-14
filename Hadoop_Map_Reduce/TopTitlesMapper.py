#!/usr/bin/env python3
import sys

lst = []

for line in sys.stdin:
    word, count = line.split('\t')
    lst.append((word, int(count)))

lst = sorted(lst, key=lambda x: x[1])
lst = lst[-10:]

for i in lst:
    print('%s\t%s' % (i[0], i[1])) #pass this output to reducer
                                                   