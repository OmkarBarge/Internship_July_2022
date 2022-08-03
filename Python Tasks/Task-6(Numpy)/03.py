'''
Topic : Transpose and Flatten

refer full question : https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true
'''

#Solution
import numpy
n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())