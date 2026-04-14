from collections import deque
from node import Node
from utils import reconstruct_path


def search(graph, coords, start, goals):
    from collections import deque
    queue = deque()
    visited = set()

    start_node = Node(start)
    queue.append(start_node)
    visited.add(start)

    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        if current.state in goals:
            return current.state, nodes_expanded, reconstruct_path(current)

        neighbors = sorted(graph[current.state], key=lambda x: x[0])

        for neighbor, cost in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(Node(neighbor, current))

    return None, nodes_expanded, []
