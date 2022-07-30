'''
Topic : Number of Students Doing Homework at a Given Time

refer full questions: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
'''
#Solution

class Solution:
    def busyStudent(startTime, endTime, queryTime):
        count = 0
        for i in range(len(startTime)):
            if (queryTime>=startTime[i]) & (queryTime<=endTime[i]):
                count+=1
        return count

st = [1,2,3]
et =[3,2,7]
qt = 4
obj = Solution
print(obj.busyStudent(st,et,qt))