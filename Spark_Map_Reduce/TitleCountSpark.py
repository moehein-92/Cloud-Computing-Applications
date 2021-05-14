#!/usr/bin/env python
'''Exectuion Command: spark-submit TitleCountSpark.py stopwords.txt delimiters
.txt dataset/titles/ dataset/output'''

import sys
from pyspark import SparkConf, SparkContext
import re
from operator import add

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

with open(stopWordsPath) as f:
    stopList = f.read().splitlines()

with open(delimitersPath) as f:
    delims = list(f.read())

def splitter(line):
    for i in delims:
        line = line.replace(i, " ")
    return line.lower()

conf = SparkConf().setMaster("local").setAppName("TitleCount")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[3], 1)
lines = lines.map(splitter)
lines = lines.flatMap(lambda x: x.split(' '))
words = lines.filter(lambda x: x is not "")
words = words.filter(lambda x: x not in stopList)
words = words.map(lambda x: (x, 1))
counts = words.reduceByKey(add)

lst = sorted(counts.collect(), key=lambda x: x[1])
lst = lst[-10:]
lst = sorted(lst, key=lambda x: x[0])

outputFile = open(sys.argv[4],"w")

for i in lst:
    outputFile.write(i[0] + "\t" + str(i[1]) + "\n")

outputFile.close()
sc.stop()