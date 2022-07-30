'''
Topic : Text Wrap

refer full question : https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
'''

#Solution

import textwrap

def wrap(string, max_width):
    return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)