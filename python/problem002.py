""" problem002.py:
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. """
from functools import lru_cache


# This lru_cache does all the memoization work.
@lru_cache()
def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def naive(max_value):
    i = 0
    out = 0
    while True:
        fib_i = fib(i)
        if fib_i > max_value:  # Exceeds 4 million. Or whatever.
            break
        if fib_i % 2 == 0:  # Add even valued term.
            out += fib_i
        i += 1
    return out

if __name__ == "__main__":
    print(naive(4000000))

