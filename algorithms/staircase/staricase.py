#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Draw a staircase of base height n and decrease the heigh of the base by 1
    for i in range(n):
        print(' ' * (n - i - 1) + '#' * (i + 1))
    
    
    

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
