""" problem4.py
        Find max{x | x is a palindrome and there exists a, b < 1000 s.t. a*b = x}.
"""

def solver():
    current_max = (91, 99)
    counter = 0
    for a in reversed(range(999)):
        for b in reversed(range(999)):
            cand = a*b
            if str(cand) == str(cand)[::-1] and cand > current_max[0]*current_max[1]:
                current_max = (a, b)
                print(current_max)
            else:
                counter += 1
    return current_max
    
if __name__ == "__main__":
    a,b = solver()
    print(a*b)
            

