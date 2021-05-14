import random 
import os
import string
import sys
import re

stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

delimiters = " \t,;.?!-:@\[\](){}_*/"

def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret

def process(userID):
    indexes = getIndexes(userID)
    #print(type(indexes[0]))
    ret = []
    lst = []
    file1 = sys.stdin.readlines()
    lines = [x.strip('\n') for x in file1]
    for line in lines:
        s1 = re.split(" \t|,|;|\.|\?|!|-|:|@|\[|\]|\(|\)|{|}|_|\*|/", line.lower())
        # ''',;.?!-:@[](){}_*/'''
        s2 = [i for i in s1 if i != ""]
        lst.append(s2)          
    #print(lst[0:30])

    dic = {}   
    for i in indexes:
        for word in lst[i]:
            if word in dic.keys():
                dic[word] += 1
            else:
                if word not in stopWordsList:
                    dic[word] = 1
    sorted_dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    #print(type(sorted_dic))
    #print(sorted_dic[:20])
    for i in range(20):
        #ret.append(sorted_dic[i])
        ret.append(sorted_dic[i][0])
    for i in ret:
        print(i)

process(sys.argv[1])
