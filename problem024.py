""" problem024.py:
        A permutation is an ordered arrangement of objects. For example, 3124
        is one possible permutation of the digits 1, 2, 3 and 4. If all of the
        permutations are listed numerically or alphabetically, we call it
        lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
            012   021   102   120   201   210

        What is the millionth lexicographic permutation of the digits 0, 1, 2,
        3, 4, 5, 6, 7, 8 and 9?
"""
from math import factorial


digits = [str(x) for x in range(10)]

# We need the millionth entry. There are 9! entries that start with 0, etc.
def main(rem):
    out = ""
    for f in range(9, -1, -1):
        fac = factorial(f)
        ind = 0
        while rem > fac and ind < len(digits)-1:
            rem -= fac
            ind += 1
        out += digits.pop(ind)
    return out


if __name__ == "__main__":
    print(main(1000000))
