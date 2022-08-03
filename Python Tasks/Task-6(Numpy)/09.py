'''
Topic : Sum and Prod

refer full question : https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true
'''

#Solution

import numpy as np
n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)],int)
print(np.prod(np.sum(arr, axis=0), axis=0))