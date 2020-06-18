""" problem010.py:
        Finds the sum of the primes below two million. """

from functools import lru_cache
from math import sqrt, ceil


def prime_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False


if __name__ == "__main__":
    print(sum(prime_sieve(2000000)))
