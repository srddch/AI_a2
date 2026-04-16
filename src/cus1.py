from collections import deque
from node import Node
from utils import reconstruct_path


def search(graph, coords, start, goals):

    reverse_graph = {}
    for u in graph:
        for v, _ in graph[u]:
            reverse_graph.setdefault(v, []).append(u)


    start_node = Node(start)
    start_queue = deque([start_node])
    start_visited = {start: start_node}

    goal_queue = deque()
    goal_visited = {}

    for g in goals:
        node = Node(g)
        goal_queue.append(node)
        goal_visited[g] = node

    nodes_expanded = 0

    while start_queue and goal_queue:

        current_node = start_queue.popleft()
        current = current_node.state
        nodes_expanded += 1

        for neighbor, _ in sorted(graph.get(current, []), key=lambda x: x[0]):

            if neighbor not in start_visited:

                child = Node(neighbor, parent=current_node)

                if neighbor in goal_visited:
                    path1 = reconstruct_path(child)
                    path2 = reconstruct_path(goal_visited[neighbor])
                    path = path1 + path2[::-1][1:]

                    return path[-1], nodes_expanded, path

                start_visited[neighbor] = child
                start_queue.append(child)

        current_node = goal_queue.popleft()
        current = current_node.state
        nodes_expanded += 1

        for neighbor in sorted(reverse_graph.get(current, [])):

            if neighbor not in goal_visited:

                child = Node(neighbor, parent=current_node)

                if neighbor in start_visited:
                    path1 = reconstruct_path(start_visited[neighbor])
                    path2 = reconstruct_path(child)
                    path = path1 + path2[::-1][1:]

                    return path[-1], nodes_expanded, path

                goal_visited[neighbor] = child
                goal_queue.append(child)

    return None, nodes_expanded, []
