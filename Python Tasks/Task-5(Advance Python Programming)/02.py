'''
Topic : Hamming Distance

refer full question : https://leetcode.com/problems/hamming-distance/
'''

#Solution

# class Solution:
#     def hammingDistance(self, x: int, y: int) -> int:
#         return bin(x^y).count('1')

class Solution:
    def hammingDistance(x,y):
        return bin(x^y).count('1')

obj = Solution
print(obj.hammingDistance(3,1))
