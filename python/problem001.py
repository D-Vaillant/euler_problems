""" problem001.py:
        Find the sum of all the multiples of 3 or 5 below 1000.
"""
from __future__ import division  # python2

def more_naive(upper, factor):
    # ??
    return sum(range(factor, factor*(upper//factor), factor))

def naive(upper, *factors):
    """ We just go through all of the integers in the range [min(factors), upper)
    and sum up the ones that are divisible by at least one factor.
    Done in O(n) time. """
    assert all(factor > 1 for factor in factors)
    return sum(i for i in range(min(factors), upper)
            if any(i%factor==0 for factor in factors))


def algebraic(upper_, factor):
    """ The objectively superior way, using Algebra.
    We take advantage of the fact that we can factor out `factor`:
        factor * (1 + ... + upper_//factor) """
    # Truncated divide to get the highest number below `upper` divisble by `factor`.
    upper = (upper_-1)//factor  
    # Using that anecdote about Gauss to get (1 + ... + upper_):
    sum_ = (1+upper) * (upper/2)
    return int(factor * sum_)


def main(max_):
    """ Only works for some values. Generalization requires some gcf magic. """
    # Principle of Inclusion/Exclusive
    return algebraic(max_, 3) + algebraic(max_, 5) - algebraic(max_, 15)


if __name__ == "__main__":
    print(main(1000))
    print(naive(1000, 3, 5))
    # This last one just plain does not work.
    # print(more_naive(1000, 3) + more_naive(1000, 5) - more_naive(1000, 15))
