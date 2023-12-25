class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __repr__(self):
        return f"{self.u} -> {self.v}: {self.w}"