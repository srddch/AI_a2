from collections import deque
from node import Node
from utils import reconstruct_path


def search(graph, coords, start, goals):
    start_node = Node(start)
    queue = deque([start_node])

    visited = {start}

    nodes_created = 1

    while queue:
        current = queue.popleft()

        if current.state in goals:
            return current.state, nodes_created, reconstruct_path(current)

        if current.state not in graph:
            continue

        neighbors = sorted(graph[current.state], key=lambda x: x[0])

        for neighbor_id, cost in neighbors:
            if neighbor_id not in visited:
                visited.add(neighbor_id)

                child_node = Node(neighbor_id, current)
                nodes_created += 1

                queue.append(child_node)

    return None, nodes_created, []
