""" problem020.py:
        Find the sum of the digits in the number 100!
"""
from math import factorial


num = factorial(100)

out = 0
for digit in str(num):
    out += int(digit)

if __name__ == "__main__":
    print(out)
