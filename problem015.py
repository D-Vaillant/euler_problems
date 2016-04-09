""" problem015.py """
# This is just a combinatorics problem. 

class GridManager():
    """ The key is MEMOIZATION! """
    """ Because before I was getting recursion errors. """
    def __init__(self):
        self.grid_dict = {}
        for _ in range(0, 22):
            self.grid_dict[(_, 0)] = 1
            self.grid_dict[(0, _)] = 1

    def get(self, n, m):
        if (n, m) not in self.grid_dict:
            self.grid_dict[(n, m)] = self.run(n, m)
        return self.grid_dict[(n, m)]

    def run(self, n, m):
        if (n-1, m) not in self.grid_dict:
            self.grid_dict[(n-1, m)] = self.run(n-1, m)
        if (n, m-1) not in self.grid_dict:
            self.grid_dict[(n, m-1)] = self.run(n, m-1)
        return self.process(n, m)

    def process(self, n, m):
        return self.grid_dict[(n, m-1)] + self.grid_dict[(n-1, m)]


if __name__ == "__main__":
    G = GridManager()
    tst = lambda x: print(G.get(x, x))
    tst(2)
    tst(3)
    tst(4)
    tst(20)
