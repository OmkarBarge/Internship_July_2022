'''
Topic : Zeros and Ones

refer full question : https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true
'''

#Solution

import numpy as np
n_m_p = tuple(map(int,input().split()))
print(np.zeros((n_m_p),dtype = np.int))
print(np.ones((n_m_p),dtype = np.int))