import heapq
from node import Node
from utils import reconstruct_path, heuristic

def search(graph, coords, start, goals):
    start_node = Node(start)
    start_node.cost = 0
    start_node.h = heuristic(start, goals, coords)
    start_node.f = start_node.cost + start_node.h
    counter = 0
    heap = [(start_node.f, counter, start, start_node)]
    visited = set()
    nodes_expanded = 0

    while heap:
        f_val, _, state, node = heapq.heappop(heap)
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
                child.cost = node.cost + cost
                child.h = heuristic(neighbor, goals, coords)
                child.f = child.cost + child.h
                heapq.heappush(heap, (child.f, counter, neighbor, child))

    return None, nodes_expanded, []