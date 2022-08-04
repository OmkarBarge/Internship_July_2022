'''
refer full question : https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem?isFullScreen=true
'''

#Solution

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

x = int(input())
n = int(input())
mu = int(input())
sigma = int(input())

mu_sum = n * mu
sigma_sum = math.sqrt(n) * sigma

def cdf(x, mu, sigma):
    Z = (x - mu)/sigma
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(cdf(x, mu_sum, sigma_sum), 4))