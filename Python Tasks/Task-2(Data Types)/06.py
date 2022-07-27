'''
Topic : Tuple

Given an integer, , and  space-separated integers as input, create a tuple, t , of those n integers.
Then compute and print the result of hast(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
'''

#Solution
n = int(input('Enter no of input to enter : '))
integer_list = map(int, input('Enter Input : ').split())
t = tuple(integer_list)
print(hash(t))