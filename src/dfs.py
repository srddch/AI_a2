from node import Node
from utils import reconstruct_path


def search(graph, coords, start, goals):
    stack = []
    visited = set()

    start_node = Node(start)
    stack.append(start_node)
    nodes_created = 1

    while stack:
        current = stack.pop()

        if current.state in visited:
            continue

        visited.add(current.state)

        if current.state in goals:
            return current.state, nodes_created, reconstruct_path(current)

        if current.state not in graph:
            continue

        neighbors = sorted(graph[current.state], key=lambda x: x[0], reverse=True)

        for neighbor_id, cost in neighbors:
            if neighbor_id not in visited:
                child_node = Node(neighbor_id, current)
                nodes_created += 1
                stack.append(child_node)

    return None, nodes_created, []
