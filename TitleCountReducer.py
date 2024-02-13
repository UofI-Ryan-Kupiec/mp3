#!/usr/bin/env python3
from operator import itemgetter
import sys

cur_token = None
cur_count = 0
token = None

# input comes from STDIN
for line in sys.stdin:
    token, count = line.split('\t', 1)
    count = int(count)
    
    if cur_token == token:
        cur_count += count
    else: 
        if cur_token:
            print ('%s\t%s' % (cur_token, cur_count))
        cur_count = count 
        cur_token = token
        
if cur_token == token:
    print('%s\t%s' % (cur_token, cur_count))