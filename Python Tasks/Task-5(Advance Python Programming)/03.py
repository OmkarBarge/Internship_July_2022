'''
Topic : Single Number II

refer full question : https://leetcode.com/problems/single-number-ii/
'''

#Solution

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         counts = collections.Counter(nums)
#
#         for key in counts:
#             if counts[key] == 1:
#                 return key
import collections
class Solution:
    def singleNumber(nums):
        counts = collections.Counter(nums)

        for key in counts:
            if counts[key] == 1:
                return key

obj = Solution
print(obj.singleNumber([1,1,1,2,2,3]))