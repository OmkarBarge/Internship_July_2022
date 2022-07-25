'''
The provided code stub reads and integer,n , from STDIN. For all non-negative integers i<n, print i ** 2 .

Example:
The list of non-negative integers that are less than  is . Print the square of each number on a separate line.
'''

n = int(input('Enter Number : '))
for i in range(n):
    if i < n:
        print(i**2)