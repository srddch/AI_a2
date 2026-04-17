import math #foundation of math functions


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
   


    lmax = compute_lmax(graph, coords)

    if lmax == 0:
        lmax = 1  # Avoid division by zero if all edges have zero length

    
    
     
   
    start_node = Node(start, None, 0)
    nodes_created = 1 # Count the start node as created
    start_node.h = heuristic(start, goals, coords) / lmax
    start_node.f = start_node.cost + start_node.h
    threshold = start_node.f
    def dfs_limited(node, threshold, path_states):
        nonlocal nodes_created

        if node.f > threshold:
            return node.f
        
        

        if node.state in goals:
            return node
        
        min_exceeded = float('inf')

        neighbors = sorted(graph[node.state], key=lambda x: x[0])

        

        for neighbor, _ in neighbors:
            if neighbor not in path_states:
                child = Node(neighbor, node, node.cost + 1)
                nodes_created += 1
                child.h = heuristic(neighbor, goals, coords) / lmax
                child.f = child.cost + child.h

                path_states.add(neighbor)
                result = dfs_limited(child, threshold, path_states)
                path_states.remove(neighbor)

                if isinstance(result, Node):
                    return result

                if result < min_exceeded:
                    min_exceeded = result

        return min_exceeded
        
    while True:
        path_states = {start}
        result = dfs_limited(start_node, threshold, path_states)

        if isinstance(result, Node):
            return result.state, nodes_created, reconstruct_path(result)
        
        if result == float('inf'):
            return None, nodes_created, []  # No solution found
        
        threshold = result
        

    

    
       