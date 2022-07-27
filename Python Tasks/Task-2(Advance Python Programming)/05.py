'''
Topic : Subtract the Product and Sum of Digits of an Integer

Given an integer number n, return the difference between the product of its digits and the sum of its digits.

refer full question : https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
'''

#Solution

# class Solution:
#     def subtractProductAndSum(self, n: int) -> int:
#         p, s = 1, 0
#         for i in str(n):
#             p *= int(i)
#             s += int(i)
#         # result = p - s
#         return (p - s)

class Solution:
    def subtractProductAndSum(n):
        p, s = 1, 0
        for i in str(n):
            p *= int(i)
            s += int(i)
        # result = p - s
        return (p - s)

n = int(input('Enter number : '))
obj = Solution
print(obj.subtractProductAndSum(n))