from node import Node
from utils import reconstruct_path


def search(graph, coords, start, goals):
    stack = []
    visited = set()

    stack.append(Node(start))
    nodes_expanded = 0

    while stack:
        current = stack.pop()

        if current.state in visited:
            continue

        visited.add(current.state)

        nodes_expanded += 1

        if current.state in goals:
            return current.state, nodes_expanded, reconstruct_path(current)

        neighbors = sorted(graph[current.state], key=lambda x: x[0], reverse=True)

        for neighbor, cost in neighbors:
            stack.append(Node(neighbor, current))

    return None, nodes_expanded, [] #第2版
