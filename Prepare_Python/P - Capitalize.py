import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    q = ""
    for i in range(0, len(s)):
        if i == 0:
            q+=s[i].upper()
        elif s[i-1] == " ":
            q+=s[i].upper()
        else:
            q+= s[i]
    return q
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()