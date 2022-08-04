'''
refer full question : https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem
'''

#Solution

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = 5
xy = [map(int, input().split()) for _ in range(n)]
sx, sy, sx2, sxy = map(sum, zip(*[(x, y, x**2, x * y) for x, y in xy]))
b = (n * sxy - sx * sy) / (n * sx2 - sx**2)
a = (sy / n) - b * (sx / n)
print('{:.3f}'.format(a + b * 80))