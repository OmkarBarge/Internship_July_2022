'''
Topic : Regex Substitution

refer full question : https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true
'''

#Solution

import re

ii = int(input())

for i in range(0,ii):
   txt = input()
   txt = re.sub(r"\ \&\&\ "," and ",txt)
   txt = re.sub(r"\ \|\|\ "," or ",txt)
   txt = re.sub(r"\ \&\&\ "," and ",txt)
   txt = re.sub(r"\ \|\|\ "," or ",txt)
   print(txt)