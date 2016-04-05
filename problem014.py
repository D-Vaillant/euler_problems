""" problem014.py:
        The following iterative sequence is defined for the set of
        positive integers:

        n -> n/2 (n is even)
        n -> 3n + 1 (n is odd)

        Using the rule above and starting with 13, we generate the following sequence:
        13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

        It can be seen that this sequence (starting at 13 and finishing at
        1) contains 10 terms. Although it has not been proved yet (Collatz
        Problem), it is thought that all starting numbers finish at 1.

        Which starting number, under one million, produces the longest chain?

        NOTE: Once the chain starts the terms are allowed to go above one million.
"""

class CollatzIterator():
    """Takes an integer, runs the Collatz iteration until termination."""
    def __init__(self, a):
        """Verifies the integer."""
        if not isinstance(a, int): raise TypeError("The non-integer case is trivial or nonsense.") 

    def __iter__(self):
        if n%2:
    def __bool__(self, a):
        return a == 1
        
