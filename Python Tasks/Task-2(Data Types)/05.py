'''
Topic : Lists

Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above.
Iterate through each command in order and perform the corresponding operation on your list.

refer full question:https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
'''

#Solution

N = int(input('Enter the no of how many operations to perform : '))
m = list()
for i in range(N):
    method, *l = input('Enter operation name and value : ').split()
    k = list(map(int, l))
    if len(k) == 2:
        q = [k[0]]
        w = [k[1]]
    elif len(k) == 1:
        q = [k[0]]
    if method == 'insert':
        m.insert(q[0], w[0])
    elif method == 'append':
        m.append(q[0])
    elif method == 'remove':
        m.remove(q[0])
    elif method == 'print':
        print(m)
    elif method == 'reverse':
        m.reverse()
    elif method == 'pop':
        m.pop()
    elif method == 'sort':
        m.sort()