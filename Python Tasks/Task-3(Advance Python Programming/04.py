'''
Topic :  Number of Steps to Reduce a Number to Zero

refer full question : https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

'''

#Solution

class Solution:
    def numberOfSteps(num):
        steps = 0
        d_v = num
        while d_v > 0:
            if d_v % 2 == 0:
                d_v =  d_v / 2
                steps+=1
            else:
                d_v = d_v - 1
                steps+=1
        return steps

obj = Solution
print(obj.numberOfSteps(14))