'''
Task : Polar Coordinates

Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.

refer full question : https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
'''
#Solution

import cmath
print(*cmath.polar(complex(input())), sep='\n')