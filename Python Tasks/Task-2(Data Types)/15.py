'''
Topic : Set .difference() Operation

refer full question : https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true
'''

#Solution

a = int(input())
b = map(int, input().split())
c = int(input())
d = map(int, input().split())
x = set(b)
y = set(d)
p = x.difference(y)
print(len(p))