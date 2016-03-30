""" problem6.py
        Find the difference between sum(range(100)^2) and sum(range(100))^2.
"""

a = (sum(range(101))**2)
b = (sum(x**2 for x in range(101)))

print(a-b)
