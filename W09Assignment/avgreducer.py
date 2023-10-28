#!/usr/bin/env python
from operator import itemgetter
import sys

#initialize vars
total_sum = 0 
total_count = 0

for line in sys.stdin:
    line = line.strip()
    sums, counts = line.split('\t')
    sums, counts = int(sums), int(counts)

    total_sum += sums
    total_count += counts

average = total_sum/total_count
print 'Average=%s' % (average)

