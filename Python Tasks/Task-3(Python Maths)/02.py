'''
Topic : Find Angle MBC

refer full question : https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
'''

#Solution

import math
a = int(input())
b = int(input())
M = math.sqrt(a**2+b**2)
theta = math.acos(b/M)
print(str(round(math.degrees(theta)))+ chr(176))