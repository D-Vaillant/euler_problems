""" problem003.py:
What is the largest prime factor of the number 600851475143? """
import math

# A lazy way would be to have a list of all the primes already.
# We only need to do the square root of that awful number.

# Another lazy way: don't bother with a prime sieve and just keep dividing.

def main(num: int):
    top = math.sqrt(num)
    lastFactor = 0
    if num % 2 == 0:
        lastFactor = 2
        num /= 2
        while num % 2 == 0:
            num /= 2
    i = 3
    while num > 1 and lastFactor <= top:
        if num % i == 0:
            lastFactor = i
            num /= i
            while num % i == 0:
                num /= i
        i += 2
    return lastFactor

if __name__ == "__main__":
    print(main(600851475143))
