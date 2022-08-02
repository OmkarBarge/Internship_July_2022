'''
Topic : Re.findall() & Re.finditer()

refer full question : https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true
'''

#Solution

import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
print(*re.findall("(?=[%s]([%s]{2,})[%s])"%(c,v,c),input(), re.I) or [-1], sep="\n")