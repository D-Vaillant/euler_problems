""" problem502.py:
    We define a block to be a rectangle with a height of 1 and an
    integer-valued length. Let a castle be a configuration of stacked blocks.

    Given a game grid that is w units wide and h units tall, a castle is
    generated according to the following rules:

        1. Blocks can be placed on top of other blocks as long as nothing sticks
           out past the edges or hangs out over open space.
        2. All blocks are aligned/snapped to the grid.
        3. Any two neighboring blocks on the same row have at least one unit
           of space between them.
        4. The bottom row is occupied by a block of length w.
        5. The maximum achieved height of the entire castle is exactly h.
        6. The castle is made from an even number of blocks.

    Let F(w,h) represent the number of valid castles, given grid parameters w and h.

    For example, F(4,2) = 10, F(13,10) = 3729050610636,
    F(10,13) = 37959702514, and F(100,100) mod 1 000 000 007 = 841913936.

    Find (F(1012,100) + F(10000,10000) + F(100,1012)) mod 1 000 000 007.
"""
from __future__ import true_division, print_function

# Use Python3!
try:
    from functools import lrucache
except ImportError:
    lrucache = memoization

def memoization(func):
    """ Simple memoization decorator. """
    memo = {}
    def mem_func(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return helper

@lrucache
def F(w, h):
    if w == 1:
        return h//2
    if h == 1: return 0 
    elif h == 2: 
        out = 0
        p = find_partitions(w)

@lrucache
def find_partitions(integer_value):
    # type: int -> generator
    """ Takes the size of the surface, generates all possible layerings. """
    for gap_count in range(integer_value):
        # 0 -> 1, 1 -> n, n-1 -> n 
    pass

""" Generate all possible outputs of the castle, while having all outputs
    obey the rules.

    First layer:
        All on. Then, various single gaps at each point.
        Then, two gaps, three gaps, and so on until n/2 gaps.
        I think this is literally an (n k) type thing...

        On that train of thought: We have boxes labeled {0..n-1}.

        The different kinds of layering correspond to how many of those 
        boxes we exclude.
        ( Since excluding all means odd blocks, ignore that.)
        Wait, so that's just binary set membership.
        So there's 2_n - 1 possibilities. (!!!)

        We can even allow these gaps to be together, to simplify
        the "double-gap" case.

    Second layer: We survived the first layer! The second layer is just recursion on each
                  surface we created.
                    So the question is, figuring out how many surfaces we create.
                  Calculate F(w_k, 2) for each of the k surfaces.
                  Then... sum them. You're adding on possibilities.
                    Without those extra castles, it'd just be empty.
                    So, the null castle represents 0 instead of 1.

"""
