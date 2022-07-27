'''
Topic : Set.add()

refer full question : https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

'''

#Solution

a = int(input())
s = set()

for i in range(a):
    val = input()
    s.add(val)

print(len(s))