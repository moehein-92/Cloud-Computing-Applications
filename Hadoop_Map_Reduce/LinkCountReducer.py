#!/usr/bin/env python3
import sys

dic ={}

for line in sys.stdin:
    origin, num_link = line.strip().split('\t')
    dic[origin] = dic.get(origin, 0) + int(num_link)

for k, v in dic.items():
    print('%s\t%s' % (k, v))