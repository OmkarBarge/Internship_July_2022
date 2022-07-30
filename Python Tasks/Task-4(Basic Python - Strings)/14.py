'''
Topic : Capitalize!

refer full question : https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
'''

#Solution


# import math
# import os
# import random
# import re
# import sys
#
# # Complete the solve function below.
# def solve(s):
#     for x in s[:].split():
#         s = s.replace(x, x.capitalize())
#     return s
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     s = input()
#
#     result = solve(s)
#
#     fptr.write(result + '\n')
#
#     fptr.close()

def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)