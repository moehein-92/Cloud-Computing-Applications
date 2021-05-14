#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext
from operator import add

conf = SparkConf().setMaster("local").setAppName("TopPopularLinks")
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

lines = lines.flatMap(splitter)
counts = lines.reduceByKey(add)
counts = counts.sortBy(lambda x: -x[1])

lst = counts.take(10)
lst = sorted(lst, key=lambda x: x[0])

output = open(sys.argv[2], "w")

#write results to output file. Foramt for each line: (key + \t + value +"\n")
for i in lst:
    output.write(i[0] + '\t' + str(i[1]) + '\n')

output.close()

sc.stop()

