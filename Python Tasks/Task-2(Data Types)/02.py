'''
Topic : Find the Runner-Up Score!
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up.

refer full question:-https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
'''

#Solution

n = int(input('Enter how many number of scores : '))
arr = map(int, input('Enter score : ').split())
arr=sorted(arr,reverse=True)
for i in range(len(arr)):
    if arr[i]==arr[0]:
        continue
    else:
        print(arr[i])
        break