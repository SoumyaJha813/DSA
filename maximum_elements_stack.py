# HackerRank - Maximum Elements (Stack)
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    # Write your code here
    A = [] #stack for pushing and poping
    max_stack = [] #stack for pushing max of current val and index [-1] val
    result = [] # return this for printing
    for operation in operations:
        oper = operation.split()
        if oper[0] == '1':
            val = int(oper[1])
            A.append(val)
            if max_stack:
                max_stack.append(max(val, max_stack[-1])) # append the max of current val and idx [-1]
            else:
                max_stack.append(val)
        elif oper[0] == '2':
            A.pop()
            max_stack.pop()
        elif oper[0] == '3':
            result.append(max_stack[-1])
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
