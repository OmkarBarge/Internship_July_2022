'''
Topic : Mean, Var, and Std

refer full question : https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true
'''

#Solution

import numpy as np
np.set_printoptions(legacy='1.12')

n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)],int)
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(round(np.std(arr), 11))