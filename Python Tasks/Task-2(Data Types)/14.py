'''
Topic : Set .intersection() Operation

refer full question : https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true
'''

#Solution

a = int(input())
b = map(int, input().split())
c = int(input())
d = map(int, input().split())
x = set(b)
y = set(d)
p = x.intersection(y)
print(len(p))
