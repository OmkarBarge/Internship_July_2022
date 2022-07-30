'''
Topic : Count Number of Teams

refer full question : https://leetcode.com/problems/count-number-of-teams/
'''

#Solution

class Solution:
    def numTeams(rating):
        import bisect
        left = []
        right = sorted(rating)
        res = 0

        for x in rating:
            right.remove(x)

            r_smaller = bisect.bisect(right, x)
            r_larger = len(right) - r_smaller

            l_smaller = bisect.bisect(left, x)
            l_larger = len(left) - l_smaller

            res += l_smaller * r_larger + l_larger * r_smaller

            left.insert(l_smaller, x)

        return res

obj = Solution
print(obj.numTeams([2,5,3,4,1]))