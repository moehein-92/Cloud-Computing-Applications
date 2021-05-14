#!/usr/bin/env python3
import sys

for line in sys.stdin:
    word, count = line.split('\t')
    print('%s\t%s' % (word, int(count))) #pass this output to reducer