class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost  # g(n)

        # 给 A* / GBFS 预留
        self.h = 0
        self.f = 0
