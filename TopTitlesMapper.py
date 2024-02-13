#!/usr/bin/env python3
import sys

for line in sys.stdin:
    word, count = line.strip().split('\t')
    print('%s\t%s' % (word, count)) 