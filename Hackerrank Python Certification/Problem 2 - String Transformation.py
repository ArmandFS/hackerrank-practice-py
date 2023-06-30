import math
import os
import random
import re
import sys

# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    # Write your code here
    l = sentence.split()
    
    li = []
    st = ""
    for i in l:
        st+=i[0]
        for j in range(0, len(i) - 1):
            if(i[j].lower()<i[j+1].lower()):
                st+=(i[j+1].upper())
            elif(i[j].lower()>i[j+1].lower()):
                st+=(i[j+1].lower())
            else:
                st+=i[j+1]
        li.append(st)
        st=""
    result=""
    
    for i in li:
        result=result+" "+i
    return (result.strip())

fptr = open(os.environ['OUTPUT_PATH'], 'w')

sentence = input()

result = transformSentence(sentence)

fptr.write(result + '\n')

fptr.close()
