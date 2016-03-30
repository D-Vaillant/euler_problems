""" problem9.py:
        Find the product of the Pythagorean triple which sums to 1000.
"""

""" Some mathematical things to note:
        We know that a + b + a^2 + b^2 = 1000, and need to find
        ab(a^2 + b^2), or ba^3 + ab^3.

        We know that a^2 + a = 1000 - b^2 - b, a(a+1) + b(b+1) = 1000.
"""

from math import sqrt

def is_square(pos_int):
    """ By Alex Martelli, http://stackoverflow.com/a/2489519 """
    x = pos_int // 2
    seen = set([x])
    while x*x != pos_int:
        x = (x + (pos_int // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

def a_finder():
    for a in range(1,400):
        for b in range(1,400):
            c = a**2 + b**2
            if is_square(c): c = round(sqrt(c))
            else: continue
            result = a + b + c
            print("{} + {} + {} = {}".format(a, b, c, result))
            if result == 1000: return (a, b, c)
    return (1, 1, 1)

a,b,c = a_finder()
print(a, b, c)
print(a*b*c)
