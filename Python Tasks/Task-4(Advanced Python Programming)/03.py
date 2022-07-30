'''
Topic : Single Number III

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
Find the two elements that appear only once. You can return the answer in any order.
You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

refer full question : https://leetcode.com/problems/single-number-iii/
'''

#Solution
# class Solution:
#     def singleNumber(self, nums: List[int]) -> List[int]:
#             return ((Counter(nums)).most_common()[-1][0],(Counter(nums)).most_common()[-2][0])


class Solution:
    def singleNumber(nums):
            return ((Counter(nums)).most_common()[-1][0],(Counter(nums)).most_common()[-2][0])

obj = Solution
print(obj.singleNumber([1,2,2,5,4,5]))