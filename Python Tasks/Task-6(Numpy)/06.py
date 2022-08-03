'''
Topic : Eye and Identity

refer full question : https://www.hackerrank.com/challenges/np-eye-and-identity/problem?isFullScreen=true
'''

#Solution:


import numpy as np
np.set_printoptions(legacy='1.13')
n,p = map(int,input().split())
print(np.eye(n,p))