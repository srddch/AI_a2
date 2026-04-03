import sys
from parser import parse_file

from bfs import search as bfs
from dfs import search as dfs
from gbfs import search as gbfs
from astar import search as astar


def main():
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        return

    filename = sys.argv[1]
    method = sys.argv[2]

    graph, coords, origin, goals = parse_file(filename)

    if method == "BFS":
        goal, nodes_expanded, path = bfs(graph, coords, origin, goals)

    elif method == "DFS":
        goal, nodes_expanded, path = dfs(graph, coords, origin, goals)

    elif method == "GBFS":
        goal, nodes_expanded, path = gbfs(graph, coords, origin, goals)
    
    elif method == "AS":
        goal, nodes_expanded, path = astar(graph, coords, origin, goals)
   
    else:
        print("Method not implemented")
        return

    print(f"{filename} {method}")
    print(f"{goal} {nodes_expanded}")
    print(" ".join(map(str, path)))


if __name__ == "__main__":
    main()