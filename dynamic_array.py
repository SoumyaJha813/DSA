#HackerRank - Dynamic Array
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for _ in range(n)]
    print("arr: ", arr)
    lastAnswer = 0
    result = []
    idx = 0
    
    for query in queries:
        query_choice, x, y = query
        idx = ((x ^ lastAnswer)% n)
        if query_choice == 1:
            arr[idx].append(y)
            print("idx: ", idx)
            print("arr[idx]: ", arr[idx])
        elif query_choice == 2:
            print("idx: ", idx)
            lastAnswer = arr[idx][y % len(arr[idx])]
            result.append(lastAnswer)
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
