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
    # Memoization dict.
    seen_before = {}

    def __init__(self, a):
        """Verifies the integer."""
        if not isinstance(a, int): raise TypeError("The non-integer case is trivial or nonsense.") 
        self.original = a
        self.a = a
        self.steps = 0

    def __next__(self):
        old = self.a
        self.steps += 1
        if self.a & 1:
            self.a = 3*self.a + 1
        else:
            self.a //= 2
        # print("{} => {}".format(old, self.a))

    def __bool__(self):
        return self.a == 1

    def run(self):
        while not (self.a in CollatzIterator.seen_before or bool(self)):
            next(self)

        try:
            total_steps = self.steps + CollatzIterator.seen_before[self.a]
            CollatzIterator.seen_before[self.original] = total_steps
            return total_steps
        except KeyError:
            CollatzIterator.seen_before[self.original] = self.steps
            return self.steps

if __name__ == "__main__":
    candidate = 0
    cand_value = 3
    for x in range(3, 1000000):
        a = CollatzIterator(x)
        series = a.run()
        if series > candidate:
            candidate = series
            cand_value = x
        else: pass

    print(cand_value)
