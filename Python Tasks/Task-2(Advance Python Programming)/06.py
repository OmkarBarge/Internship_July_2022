'''
Topic : XOR Operation in an Array

You are given an integer n and an integer start.
Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.
Return the bitwise XOR of all elements of nums.

refer full question : https://leetcode.com/problems/xor-operation-in-an-array/
'''

#Solution
#
# class Solution:
#     def xorOperation(self, n: int, start: int) -> int:
#         nums = []
#         for i in range(n):
#             nums.append(start + (2 * i))
#         XOR = nums[0]
#         for i in range(1,len(nums)):
#             XOR ^= nums[i]
#         return (XOR)

class Solution:
    def xorOperation(n, start):
        nums = []
        for i in range(n):
            nums.append(start + (2 * i))
        XOR = nums[0]
        for i in range(1,len(nums)):
            XOR ^= nums[i]
        return (XOR)
n = int(input('Enter how many element to add : '))
s = int(input('Enter Start Number : '))
obj = Solution
print(obj.xorOperation(n , s))