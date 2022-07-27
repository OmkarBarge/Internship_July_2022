'''
Topic : Introduction to set

refer full question : https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
'''

#Solution

def average(array):
    # your code goes here
    x=set(array)
    return float(sum(x)/len(x))

if __name__ == '__main__':
    # n = int(input('Enter how many entry want to enter : '))
    arr = list(map(int, input('Enter values to get average : ').split()))
    result = average(arr)
    print(result)