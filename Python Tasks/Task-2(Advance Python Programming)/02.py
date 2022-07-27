'''
Topic : Find Numbers with Even Number of Digits

Given an array nums of integers, return how many of them contain an even number of digits.

refer full question : https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
'''

#Solution

# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         even = 0
#         for i in nums:
#             i = str(i)
#             if len(i) % 2 == 0:
#                 even += 1
#
#         return even

class Solution:
    def findNumbers(nums):
        even = 0
        for i in nums:
            i = str(i)
            if len(i) % 2 == 0:
                even += 1

        return even

numbers = [12,345,2,6,7896]
obj = Solution
print(Solution.findNumbers(numbers))