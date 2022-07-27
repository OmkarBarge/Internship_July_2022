'''
Topic : Set .union() Operation

The students of District College have subscriptions to English and French newspapers.
Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers.
One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper.
The same student could be in both sets.
Your task is to find the total number of students who have subscribed to at least one newspaper.

refer full question : https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true
'''

a = int(input())
b = map(int, input().split())
c = int(input())
d = map(int, input().split())
x = set(b)
y = set(d)
p = x.union(y)
print(len(p))