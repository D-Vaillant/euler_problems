""" problem026.py:
        A unit fraction contains 1 in the numerator. The decimal representation
        of the unit fractions with denominators 2 to 10 are given:
            1/2 = 0.5
            1/3 = 0.(3)
            1/4 = 0.25
        Find the value of d < 1000 for which 1/d contains the longest recurring
        cycle in its decimal fraction part.
"""
# Use the Euclidean division algorithm.
def relativize(n, m):
    """ Returns the relativized n and how many powers we increased it by. """
    count = 0
    while n < m:
        n *= 10
        count += 1
    return n, count

def euclidean_alg(n, m):
    """ returns a, b such that a*m + b = n """
    if m > n:
        n, m = m, n

    a = 0
    while n >= m:
        n -= m
        a += 1
    return a, n

def create_decimal(denom):
    b = -1
    count = 0
    while b != 0 or count < 10:
