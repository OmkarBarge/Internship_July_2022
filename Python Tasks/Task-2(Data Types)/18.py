'''
Topic : Check Subset
refer full question : https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
'''

#Solution

for _ in range(int(input())):
    x, a, z, b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))