""" problem025.py:
       What is the index of the first term in the Fibonacci sequence
       to contain 1000 digits? 
"""
from functools import lru_cache

@lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

def over_1000_digits(n):
    return len(str(n)) >= 1000

if __name__ == "__main__":
    n = 0
    F = fib(n)
    while not over_1000_digits(F):
        n += 1
        F = fib(n)

    print(n)
