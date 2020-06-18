""" problem067.py:
        Find the maximum total from top to bottom in triangle.txt, a 15K text
        file containing a triangle with one-hundred rows.
"""

from problem018 import make_pt
file_ = "p067_triangle.txt"

with open(file_) as F:
    Q = F.readlines()
    # This part is kind of complicated but it does something really simple:
    #      It takes an array of strings, removes '\n' from the end,
    #      splits up the string into an array of words. Then it maps
    #      int over this word array and turns that into a tuple.
    # It does this for each row of the text document.
    W = (tuple(map(int, q.strip().split()) for q in Q)) 
    print(make_pt(W)[-1])
