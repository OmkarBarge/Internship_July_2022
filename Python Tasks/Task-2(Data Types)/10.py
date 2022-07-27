'''
Topic : Symmetric Difference
refer full question : https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true
'''

#Solution

a,b=(int(input()),input().split())
c,d=(int(input()),input().split())
x=set(b)
y=set(d)
p=y.difference(x)
q=x.difference(y)
r=p.union(q)
print ('\n'.join(sorted(r, key=int)))

