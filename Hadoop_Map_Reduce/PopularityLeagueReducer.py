#!/usr/bin/env python3
import sys

dic = {}
# input comes from STDIN
for line in sys.stdin:
    link, num_link = line.split('\t')
    dic[link] = int(num_link)

lst = sorted(dic.items(), key=lambda x: x[1])

dic = {}
rank, count, previous = 0, -1, None

for key, num in lst:
    count += 1
    if num != previous: 
        rank += count
        previous = num
        count = 0
    dic[key] = rank

sorted_dic = sorted(dic.items(), key=lambda x: int(x[0]), reverse=True)

for i in sorted_dic:
    print('%s\t%s' % (i[0], i[1]))