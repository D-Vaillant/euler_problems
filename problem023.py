""" problem023.py:
        A number n is called deficient if the sum of its proper divisors is
        less than n and it is called abundant if this sum exceeds n.

        As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
        smallest number that can be written as the sum of two abundant numbers
        is 24. By mathematical analysis, it can be shown that all integers
        greater than 28123 can be written as the sum of two abundant numbers.

        However, this upper limit cannot be reduced any further by analysis
        even though it is known that the greatest number that cannot be
        expressed as the sum of two abundant numbers is less than this limit.

        Find the sum of all the positive integers which cannot be written as
        the sum of two abundant numbers.
"""
from math import ceil, sqrt


def factor(n):
    factors = [1]
    for x in range(2, ceil(sqrt(n))+1):
        if (n % x == 0):
            factors.extend(list({x, n//x}))
    return set(factors)


abundances = [x for x in range(12, 28123) if sum(factor(x)) > x]


def is_not_sum_of_abundant_nums(num):
    print("Doing num {}".format(num))
    for i in filter(lambda x: x < num, abundances):
        if num-i in abundances:
            return False
        if num-i < i:
            return True


if __name__ == "__main__":
    counterbunds = (filter(is_not_sum_of_abundant_nums, range(12, 28123)))
    print(sum(counterbunds))
