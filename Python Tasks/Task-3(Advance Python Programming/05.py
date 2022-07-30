'''
Topic : Counting Bits

refer full question : https://leetcode.com/problems/counting-bits/
'''

#Solution

class Solution:
    def countBits(n):
        res=[]
        for i in range(n+1):
            res.append(format(i,"b").count("1"))
        return res

obj = Solution
print(obj.countBits(5))