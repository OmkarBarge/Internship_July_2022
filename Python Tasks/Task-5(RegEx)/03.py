'''
Topic : Group(), Groups() & Groupdict()

refer full question : https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true
'''

#Solution

import re
m = re.findall(r"([A-Za-z0-9])\1+",input())
if m:
    print(m[0])
else:
    print(-1)