'''
'Question'
Task
Given an integer,n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20 , print Not Weird.
'''

n = int(input('Enter Number : '))

if n % 2 == 0:
    if (n >= 2 and n <= 5) or (n > 20):
        print('Not Weird')
    else:
        print('Weird')
else:
    print('Weird')