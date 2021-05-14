#!/usr/bin/env python

#Execution Command: spark-submit PopularityLeagueSpark.py dataset/links/ dataset/league.txt
import sys
from pyspark import SparkConf, SparkContext
from operator import add

conf = SparkConf().setMaster("local").setAppName("PopularityLeague")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[1], 1) 

def splitter(line):
    origin, branch = line.split(':')
    branch = branch.split()
    lst = []
    if origin in branch:
        lst.append((origin, 1))
    else:
        lst.append((origin, 0))
    for b in branch:
        lst.append((b, 1))
    return lst

leagueIds = sc.textFile(sys.argv[2], 1)
leagueList = leagueIds.collect()


lines = lines.flatMap(splitter)
counts = lines.reduceByKey(add)
counts = counts.filter(lambda x: x[0] in leagueList)

lst = counts.collect()
lst = sorted(lst, key=lambda x: x[1])

dic = {}
rank, count, previous = 0, -1, None

for key, num in lst:
    count += 1
    if num != previous: 
        rank += count
        previous = num
        count = 0
    dic[key] = rank

sorted_dic = sorted(dic.items(), key=lambda x: x[0])

#print(sorted_dic)

output = open(sys.argv[3], "w")
for i in sorted_dic:
    output.write(i[0] + '\t' + str(i[1]) + '\n')

output.close()

sc.stop()

