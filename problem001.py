""" problem001.py:
        Find the sum of all the multiples of 3 or 5 below 1000.
"""
from __future__ import division  # lol python2


def arith(lower, upper):
    while upper%lower:
        upper -= 1
    # print("({} + {})/2 * {}".format(lower, upper, upper/lower))
    return (lower + upper)/2 * (upper/lower)


def main(max_):
    return arith(3, max_) + arith(5, max_) - arith(15, max_)


if __name__ == "__main__":
    print(main(999))
