""" problem97.py:
        The first known prime found to exceed one million digits was discovered
        in 1999, and is a Mersenne prime of the form (2**6,972,593)-1.
        It contains exactly 2,098,960 digits. Subsequently other Mersenne
        primes, of the form (2**P)-1, have been found which contain more digits.

        However, in 2004 there was found a massive non-Mersenne prime which
        contains 2,357,207 digits: 28433*(2**7830457)+1

        Find the last ten digits of this prime number.
"""

# Thoughts
"""
The key to this one seems to be memory management. I surely can't calculate
that prime number. What I can do is calculate the last ten digits.

Break up the problem into sub-problems where we only store the last eleven
digits and do the math that way. 
"""

def truncater(x):
    return x%(10**12)

if __name__ == "__main__":
    a = truncater(2**7830457) # sorry
    print((28433*a + 1)%(10**11))
