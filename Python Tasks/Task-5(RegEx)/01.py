'''
Topic : Detect Floating Point Number

You are given a string N.
Your task is to verify that N is a floating point number.

refer full question : https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true
'''

#Solution

import re
for _ in range(int(input())):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))