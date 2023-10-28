#!/usr/bin/env python

import sys



for line in sys.stdin:
    line = line.strip()
    nums = line.split(',')
    ints = []
    for num in nums:
        
        try:
            
            i = int(num)
#            print '%s\t%s' % (i, 1)
            ints.append(i)
            sums = sum(ints)
            counts = len(ints)

        except:
            pass #skip if the value passed is not an integer



    print '%s\t%s' % (sums, counts)  
