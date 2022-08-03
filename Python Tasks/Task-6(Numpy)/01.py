'''
Topic : Arrays

refer full question : https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true
'''

#Solution

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = numpy.array(arr,float)
    return arr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)