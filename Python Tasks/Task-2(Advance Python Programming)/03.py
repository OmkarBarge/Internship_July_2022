'''
Topic : Number of Good Pairs

Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.

refer full question : https://leetcode.com/problems/number-of-good-pairs/
'''

#Solution

# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         good_pair = 0
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j] and i < j:
#                     good_pair += 1
#
#         return good_pair

class Solution:
    def numIdenticalPairs(nums):
        good_pair = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    good_pair += 1

        return good_pair
l = [1,2,3,1,1,3]
obj = Solution
print(obj.numIdenticalPairs(l))
