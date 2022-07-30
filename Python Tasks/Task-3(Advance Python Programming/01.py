'''
Topic : Maximum Product of Two Elements in an Array

Given the array of integers nums, you will choose two different indices i and j of that array.
Return the maximum value of (nums[i]-1)*(nums[j]-1).

refer full question : https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
'''

#Solution - 1

class Solution:
    def maxProduct(nums):
        x,y = max(nums), min(nums)
        counter = 0
        for num in nums:
            if num == x:
                counter+=1
            if (num>y)&(num!=x):
                y=num
        if counter>1:
            y=x
        return (x-1)*(y-1)

n = [3,4,5,2]
obj = Solution
print(obj.maxProduct(n))
