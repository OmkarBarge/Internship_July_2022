'''
Topic : Finding the percentage

The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

refer full question: https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

'''

#Solution
n = int(input('Enter how many entry to enter : '))
student_marks = {}
for _ in range(n):
    name, *line = input('Enter name and score : ').split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input('Enter name to get the average : ')

l = []
for i in student_marks[query_name]:
    l.append(i)

l_len = len(l)
s = sum(l)
result = s/l_len
print("{:.2f}".format(result))