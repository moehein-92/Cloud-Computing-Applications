#!/usr/bin/env python3
import sys

dic ={}

for line in sys.stdin:
    origin, branch = line.split(':')
    branch = branch.split()
    origin = int(origin)

    if origin not in dic:
        dic[origin] = set()
    
    for v in branch:
        v = int(v)
        if v is origin:
            continue
        if v not in dic:
            dic[v] = set()
        dic[v].add(origin)

for k in dic:
    print('%s\t%s' % (k, len(dic[k])))