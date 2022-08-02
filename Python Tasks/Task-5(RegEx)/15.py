'''
Topic : Validating Credit Card Numbers

refer full question : https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true
'''

#Solution

import re
TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for _ in range(int(input().strip())):
    print("Valid" if TESTER.search(input().strip()) else "Invalid")