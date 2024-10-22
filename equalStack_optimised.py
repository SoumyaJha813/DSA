#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def getCumulativeHeight(stack):
    current_sum = 0
    cummulative_height = []
    for st in reversed(stack):
        current_sum += st
        cummulative_height.append(current_sum)
    return cummulative_height
        
def equalStacks(h1, h2, h3):
    # Write your code here
    heights1 = set(getCumulativeHeight(h1))
    heights2 = set(getCumulativeHeight(h2))
    heights3 = set(getCumulativeHeight(h3))
    
    commonHeight = heights1.intersection(heights2, heights3)
    if commonHeight:
        return max(commonHeight)
    else:
        return 0
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
