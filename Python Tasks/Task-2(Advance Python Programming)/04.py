'''
Topic : How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.

refer full question : https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
'''




#Solution

# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         final_output = []
#         for i in range(len(nums)):
#             count = 0
#             for j in range(len(nums)):
#                 if nums[j] < nums[i]:
#                     count+=1
#             final_output.append(count)
#
#         return final_output

nums = [8,1,2,2,3]
final_output = []
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[j] < nums[i]:
            count+=1
    final_output.append(count)

print(final_output)