#!/usr/bin/env python3
import sys

top_n = {}
for line in sys.stdin:
    word, count = line.strip().split('\t')
    top_n[word] = int(count)
    
top_n = sorted(top_n.items(), key=lambda item: (item[1], item[0]))[-10:]
for word, count in top_n:
    print('%s\t%s' % (word, count))