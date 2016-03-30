""" problem010.py:
        Finds the sum of the primes below two million. """

def main():
    """Implements a sieve to find the primes, sums them while doing so."""
    primes = [p for p in range(2000000) if isPrime(p)]
    return sum(primes)

def isPrime(n):
    """Implementation of a naive primality test."""
    if n <= 1: return False
    elif n <= 3: return True
    elif n%2 == 0 or n%3 == 0: return False

    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0: return False
        i += 6
    return True

if __name__ == "__main__":
    print(main())
