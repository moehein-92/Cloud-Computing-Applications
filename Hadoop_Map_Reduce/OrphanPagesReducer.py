#!/usr/bin/env python3
import sys

dic ={}
orphans = []

for line in sys.stdin:
    origin, num_link = line.strip().split('\t')
    dic[origin] = dic.get(origin, 0) + int(num_link)

dic_items = dic.items()
sorted_dic = sorted(dic_items)
for k, v in sorted_dic:
    if dic.get(k) == 0:
        orphans.append(k)

for i in sorted(orphans, key=lambda x: int(x)):
    print(i)

