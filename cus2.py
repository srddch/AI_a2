import math #foundation of math functions
import heapq #Import Python's "heap" tool, which is usually used to create a priority queue

from node import Node #import node from node.py
from utils import reconstruct_path, heuristic #reconstruct_path: perform a whole path, heuristic: return the straightline distance between two points



def compute_lmax(graph, coords):  #compute the geometric length of the "longest true edge" in the entire picture
    max_len =0    #think the current len is 0, then compare

    for u in graph:    #Traverse each starting node in the graph
        x1, y1 = coords[u]   #orginal 

        for v, _ in graph[u]:  #v is the final point
            x2, y2 = coords[v]    #final point
            edge_len = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            if edge_len > max_len:
                max_len = edge_len

    return max_len


def search(graph, coords, start, goals):
   

    """
    CUS2:
    An informed search method for finding a shortest path
    with the least number of moves.
    """

    lmax = compute_lmax(graph, coords)

    if lmax == 0:
        lmax = 1  # Avoid division by zero if all edges have zero length

    frontier = []  #empty list
    order = 0  # To keep track of the order of node expansion
    nodes_expanded = 0  #originally no nodes are expanded
    visited = set()  #keep track of visited nodes

    start_node = Node(start, None, 0)
    start_node.h = heuristic(start, goals, coords) / lmax
    start_node.f = start_node.cost + start_node.h

    heapq.heappush(frontier, (start_node.f, start_node.state, order, start_node))

    while frontier:
        _, _, _, current = heapq.heappop(frontier)

        if current.state in visited:
            continue

        visited.add(current.state)
        nodes_expanded += 1

        if current.state in goals:  #check if the current node is a goal
            return current.state, nodes_expanded, reconstruct_path(current)
        

        neighbors = sorted(graph[current.state], key=lambda x: x[0])  #sort the neighbors in ascending node order

        for neighbor, _ in neighbors:
            if neighbor not in visited:
                child = Node(neighbor, current, current.cost + 1)
                child.h = heuristic(neighbor, goals, coords) / lmax
                child.f = child.cost + child.h

                order += 1
                heapq.heappush(frontier, (child.f, child.state,order, child))

    return None, nodes_expanded, []