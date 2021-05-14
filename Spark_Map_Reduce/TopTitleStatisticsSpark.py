#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("TopTitleStatistics")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[1], 1)

dic = {}
dic2 = {}
for i in lines.collect():
    word, count = i.split('\t')
    dic[word] = int(count)

Sum = sum(dic.values())
Mean = Sum/(len(dic))

dic2['Mean'] = int(Mean)
dic2['Sum'] = int(Sum)
dic2['Min'] = int(min(dic.values()))
dic2['Max'] = int(max(dic.values()))

variance = 0
for i in dic.values():
    variance += ((Mean-i)**2)/len(dic)

dic2['Var'] = int(variance)

outputFile = open(sys.argv[2], "w")

for k, v in dic2.items():
    outputFile.write(k + "\t" + str(v) + "\n")

outputFile.close()
sc.stop()
