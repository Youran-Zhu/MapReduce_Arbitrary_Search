#!/usr/bin/env python
"""mapper.py"""

import sys
import re

arg_list = sys.argv[1:]

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        flag = False
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for i in arg_list:
            if re.search(i, word):
                flag = True
                break
        if flag or len(arg_list) == 0:
            print '%s\t%s' % (word, 1)
        else:
            print '%s\t%s' % (word, 0)
