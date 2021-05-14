#!/usr/bin/env python3
import sys
import math

dic = {}
dic2 = {}
Sum = 0
for line in sys.stdin:
    word, count = line.split('\t')
    count = int(count)
    dic[word] = count
    Sum += count
    
Mean = Sum/(len(dic))

dic2['Mean'] = int(Mean)
dic2['Sum'] = int(Sum)
dic2['Min'] = int(min(dic.values()))
dic2['Max'] = int(max(dic.values()))

variance = 0
for i in dic.values():
    variance += ((Mean-i)**2)/len(dic)

dic2['Var'] = int(variance)

for k, v in dic2.items():
    print('%s\t%s' % (k, v)) # print as final output

