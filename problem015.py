""" problem015.py """
# This is just a combinatorics problem. 

class GridShape():
    def __init__(self, down = None, right = None):
        self.d = down
        self.r = right

        self.paths = 0
        try: self.paths += self.d.paths
        except AttributeError: pass

        try: self.paths += self.r.paths
        except AttributeError: pass

        if self.paths == 0 : raise Exception("Call SquareShape instead.")

class SinglePath(GridShape):
    def __init__(self, **kwargs):
        self.paths = 1

class SquareShape(GridShape):
    def __init__(self, **kwargs):
        self.d = None
        self.r = None
        self.paths = 2

class GridManager():
    """ The key is MEMOIZATION! """
    """ Because before I was getting recursion errors. """
    def __init__(self):
        self.grid_dict = {}
        self.grid_dict[(2, 2)] = SquareShape()
        for _ in range(1, 23):
            self.grid_dict[(_, 1)] = SinglePath()
            self.grid_dict[(1, _)] = SinglePath()

    def run(self, n, m):
        try: return self.grid_dict[(n,m)]
        except KeyError: pass

        if (n-1, m) not in self.grid_dict:
            self.grid_dict[(n-1, m)] = self.run(n-1, m)
        if (n, m-1) not in self.grid_dict:
            self.grid_dict[(n, m-1)] = self.run(n, m-1)
        return self.process(n, m)

    def process(self, n, m):
        return GridShape(down = self.grid_dict[(n, m-1)],
                         right = self.grid_dict[(n-1, m)])


if __name__ == "__main__":
    G = GridManager()
    print(G.run(21, 21).paths)
