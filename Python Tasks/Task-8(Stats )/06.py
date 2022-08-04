'''
refer full question : https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem?isFullScreen=true
'''

#Solution

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

numTic = float(input())
numStd = float(input())
mu = numStd * float(input())
sig = math.sqrt(numStd) * float(input())

print(round(0.5*(1+math.erf((numTic - mu)/(sig * math.sqrt(2)))),4))
