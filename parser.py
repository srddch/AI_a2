def parse_file(filename):
    graph = {}
    coords = {}
    origin = None
    goals = []

    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    mode = None

    for line in lines:
        if line.startswith("Nodes:"):
            mode = "nodes"
            continue
        elif line.startswith("Edges:"):
            mode = "edges"
            continue
        elif line.startswith("Origin:"):
            mode = "origin"
            continue
        elif line.startswith("Destinations:"):
            mode = "goals"
            continue

        if mode == "nodes":
            node, coord = line.split(":")
            x, y = coord.strip()[1:-1].split(",")
            node_id = int(node)
            coords[node_id] = (int(x), int(y))
            graph[node_id] = []

        elif mode == "edges":
            part, cost = line.split(":")
            n1, n2 = part.strip()[1:-1].split(",")
            graph[int(n1)].append((int(n2), int(cost)))

        elif mode == "origin":
            origin = int(line)

        elif mode == "goals":
            goals = [int(x.strip()) for x in line.split(";")]

    return graph, coords, origin, goals