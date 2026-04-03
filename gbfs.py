import heapq
from node import Node
from utils import reconstruct_path, heuristic

def search(graph, coords, start, goals):
    start_node = Node(start)
    start_node.h = heuristic(start, goals, coords)
    counter = 0
    heap = [(start_node.h, counter, start, start_node)]
    visited = set()
    nodes_expanded = 0

    while heap:
        h_val, _, state, node = heapq.heappop(heap)
        if state in visited:
            continue
        visited.add(state)
        nodes_expanded += 1

        if state in goals:
            return state, nodes_expanded, reconstruct_path(node)

        neighbors = sorted(graph[state], key=lambda x: x[0])
        for neighbor, cost in neighbors:
            if neighbor not in visited:
                counter += 1
                child = Node(neighbor, node)
                child.h = heuristic(neighbor, goals, coords)
                heapq.heappush(heap, (child.h, counter, neighbor, child))

    return None, nodes_expanded, []