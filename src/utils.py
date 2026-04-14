import math

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]


def heuristic(n, goals, coords):
    x1, y1 = coords[n]
    return min(
        math.sqrt((x1 - coords[g][0])**2 + (y1 - coords[g][1])**2)
        for g in goals
    )
