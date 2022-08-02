'''
Topic : Validating and Parsing Email Addresses

refer full question : https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true
'''

#Solution:

import re
n = int(input())
for _ in range(n):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)