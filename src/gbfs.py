import heapq
from node import Node
from utils import reconstruct_path, heuristic

def search(graph, coords, start, goals):
    start_node = Node(start)
    start_node.h = heuristic(start, goals, coords)
    counter = 0
    heap = [(start_node.h, counter, start, start_node)]
    visited = set()
    nodes_created = 1  # 起始节点已创建

    while heap:
        h_val, _, state, node = heapq.heappop(heap)
        if state in visited:
            continue
        visited.add(state)

        if state in goals:
            return state, nodes_created, reconstruct_path(node)

        neighbors = sorted(graph[state], key=lambda x: x[0])
        for neighbor, cost in neighbors:
            if neighbor not in visited:
                counter += 1
                child = Node(neighbor, node)
                nodes_created += 1  # 子节点创建时计数
                child.h = heuristic(neighbor, goals, coords)
                heapq.heappush(heap, (child.h, counter, neighbor, child))

    return None, nodes_created, []
