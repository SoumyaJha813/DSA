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

def equalStacks(h1, h2, h3):
    # Write your code here
    h1, h2, h3 = h1[::-1], h2[::-1], h3[::-1]
    total1, total2, total3 = sum(h1), sum(h2), sum(h3)
    while not (total1 == total2 == total3):
        if total1 >= total2 and total1>= total3:
            total1 -= h1.pop()
        elif total2 > total1 and total2> total3:
            total2 -= h2.pop()
        elif total3 > total1 and total3> total2:
            total3 -= h3.pop()
        if total1 == 0 or total2 ==0 or total3 ==0:
            return 0
    return total1
    
    

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
