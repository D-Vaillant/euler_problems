""" problem016.py:
        2**15 = 32,768 and the sum of its digits is 3 + 2 + 6 + 8 = 26.

        What is the sum of the digits of the number 2**1000?
"""

def brute_force():
    """Because computers are fast and man is lazy."""
    return sum(int(x) for x in str(2**1000))

if __name__ == "__main__":
    print("Hold on...")
    print(brute_force())
