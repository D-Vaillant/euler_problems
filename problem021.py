""" problem021.py:
        Let d(n) be defined as the sum of proper divisors of n.

        If d(a) = b and d(b) = a, where a !=  b, then a and b are an
        amicable pair and each of a and b are called amicable numbers.

        For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
        22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of
        284 are 1, 2, 4, 71 and 142; so d(284) = 220.

        Evaluate the sum of all the amicable numbers under 10000.
"""
from math import sqrt, ceil


def factor(n):
    factors = [1]
    for x in range(2, ceil(sqrt(n))+1):
        if (n % x == 0):
            factors.extend(list({x, n//x}))
    return factors

def amicable_list(n):
    sum_fac = sum(factor(n))
    if sum_fac <= n:
        return []
    return [n, sum_fac] if sum(factor(sum_fac)) == n else []


if __name__ == "__main__":
    amicables = []
    for num in range(2, 10000):
        amicables.extend(amicable_list(num))

    print(sum(amicables))
