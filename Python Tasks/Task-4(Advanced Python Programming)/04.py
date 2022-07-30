'''
Topic: Subsets

refer full question : https://leetcode.com/problems/subsets/
'''

#Solution

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
                return [lst for lsts in [list(combinations(nums,i)) for i in range(len(nums)+1)] for lst in lsts]
