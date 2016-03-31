""" problem012.py:
        The sequence of triangle numbers is generated by adding the natural numbers.
        So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

        The first ten terms would be:
        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

        Let us list the factors of the first seven triangle numbers:

             1: 1
             3: 1,3
             6: 1,2,3,6
            10: 1,2,5,10
            15: 1,3,5,15
            21: 1,3,7,21
            28: 1,2,4,7,14,28

        We can see that 28 is the first triangle number to have over five divisors.

        What is the value of the first triangle number to have over five hundred divisors?
"""

# Two problems here:
#   1. Generate triangle numbers.
#   2. Find factors of triangle number, count the number of factors.

from math import sqrt

def triangle_number_generator(num):
    """lol, Python."""
    return sum(range(1, num+1))

def factorize(n):
    out_list = []
    for i in range(1, int(sqrt(n) + 1)):
        if n%i == 0:
            out_list.extend([i, n//i])
    return set(out_list)

def main(divisors = 500, init_num = 1):
    divies = 0
    out = None
    i = init_num - 1
    while divies < 500:
        i += 1
        out = triangle_number_generator(i)
        cand = len(factorize(out))
        if cand > divies: divies = cand
    return out

if __name__ == "__main__":
    print(main())
