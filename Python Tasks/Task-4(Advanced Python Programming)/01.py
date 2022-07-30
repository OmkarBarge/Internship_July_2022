'''
Topic : Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space

refer full question : https://leetcode.com/problems/single-number/
'''

# Solution

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         return reduce(lambda total, el: total ^ el, nums)

class Solution:
    def singleNumber(nums):
        return reduce(lambda total, el: total ^ el, nums)

obj = Solution
print(obj.singleNumber([1,2,2,3]))