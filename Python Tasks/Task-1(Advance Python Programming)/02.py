'''
Topic: Shuffle the Array
'Question'
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

'Example'
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
'''

#Solution

#LeetCode Solution

# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         n_l = len(nums)
#         output_list = []
#
#         for i in range(n_l):
#             if i < n:
#                 output_list.append(nums[i])
#                 output_list.append(nums[n + i])
#
#         return output_list

#LeetCode Executed

class Solution:
    def shuffle(nums,n):
        n_l = len(nums)
        output_list = []

        for i in range(n_l):
            if i < n:
                output_list.append(nums[i])
                output_list.append(nums[n + i])

        return output_list

nums = [1,2,3,4,5,6]
n = 3

obj = Solution
print(obj.shuffle(nums,n))