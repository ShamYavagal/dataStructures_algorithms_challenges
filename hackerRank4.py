#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

'''
def countingValleys(steps, path):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
 

path = list('UDUUUDUDDD')

up = 0
down = 0

valley = 0
mountain = 0

for index, each in enumerate(path):
    if each == 'U':
        down -= 1
    elif each == 'D':
        down += 1
    if each == 'U' and down == 0:
        valley += 1
    if each == 'D' and down == 0:
        mountain += 1

print(valley)
''' 

def countingValleys(path):
    up = 0
    down = 0

    valley = 0
    mountain = 0

    for index, each in enumerate(path):
        if each == 'U':
            down -= 1
        elif each == 'D':
            down += 1
        if each == 'U' and down == 0:
            valley += 1
        if each == 'D' and down == 0:
            mountain += 1
    return valley