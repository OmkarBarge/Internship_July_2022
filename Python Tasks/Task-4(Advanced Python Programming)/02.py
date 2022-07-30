'''
Topic : Sort Integers by The Number of 1 Bits

You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation
and in case of two or more integers have the same number of 1's you have to sort them in ascending order.
Return the array after sorting it.

refer full question : https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
'''
#Solution

# class Solution:
#     def sortByBits(self, arr: List[int]) -> List[int]:
#         return sorted(arr, key = lambda x: (bin(x).count('1'), x))

class Solution:
    def sortByBits(arr):
        return sorted(arr, key = lambda x: (bin(x).count('1'), x))

obj = Solution
print(obj.sortByBits([0,1,2,5,8,6,5,4,7,]))
