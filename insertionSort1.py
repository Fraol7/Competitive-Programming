#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(num, a_list):
    temp = a_list[-1]
    i = num-1
    while i > 0 and a_list[i-1] > temp:
        a_list[i] = a_list[i-1]
        print(*a_list)
        i -= 1
    a_list [i] = temp
    print(*a_list)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
