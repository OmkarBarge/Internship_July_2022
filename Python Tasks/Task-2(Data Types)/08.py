'''
Topic : Set .symmetric_difference() Operation

The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
The set is immutable to the .symmetric_difference() operation (or ^ operation).

refer full question : https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true
'''

#Solution

m=input()
eng_new = input().split()
s1 = set(eng_new)
n=input()
fre_new = input().split()
s2 = set(fre_new)
s1s2 = s1.symmetric_difference(s2)
print(len(s1s2))