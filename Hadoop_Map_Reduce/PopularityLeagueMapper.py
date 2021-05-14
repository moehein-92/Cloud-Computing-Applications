#!/usr/bin/env python3
import sys

leaguePath = sys.argv[1]

with open(leaguePath) as f:
    league_list = f.read().splitlines()

dic = {}

for line in sys.stdin:
    link, num_link = line.split('\t')
    dic[link] = int(num_link)

for i in league_list:
    if i in dic:
        print('%s\t%s' % (i, dic[i]))

