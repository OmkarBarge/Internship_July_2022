'''
Topic : Concatenate

refer full question : https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=numpy
'''

#Solution

import numpy as np
n,m,p = map(int,input().split())
arr_1 = np.array([input().split() for _ in range(n)],int)
arr_2 = np.array([input().split() for _ in range(m)],int)

print(np.concatenate((arr_1,arr_2),axis=0))