'''
Topic : Check Strict Superset

refer full question : https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
'''

#Solution

a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))
