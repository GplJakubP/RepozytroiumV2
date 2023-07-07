def dfs(graph):
    for u in graph:
        u['p'] = None
        u['visited'] = False
        u['time_entry'] = None
        u['time_exit'] = None
    time = 0

    for u in graph:
        if not u['visited']:
            time = dfs_explore(u, time)

def dfs_explore(u, time):
    time += 1
    u['time_entry'] = time
    u['visited'] = True

    for v in u['neighbors']:
        if not v['visited']:
            v['p'] = u
            time = dfs_explore(v, time)

    time += 1
    u['time_exit'] = time

    return time

def create_graph():
    num_vertices = int(input("Podaj liczbę wierzchołków w grafie: "))
    graph = []

    for i in range(num_vertices):
        vertex = {'id': chr(ord('a') + i), 'neighbors': []}
        num_neighbors = int(input(f"Podaj liczbę sąsiadów dla wierzchołka {vertex['id']}: "))

        if num_neighbors == 1:
            print(f"Wierzchołek {vertex['id']} graniczy tylko z jednym wierzchołkiem.")
            neighbor_id = input(f"Podaj identyfikator tego wierzchołka: ")
            neighbor_vertex = next((v for v in graph if v['id'] == neighbor_id), None)
            if neighbor_vertex is not None:
                vertex['neighbors'].append(neighbor_vertex)
                neighbor_vertex['neighbors'].append(vertex)
        else:
            for j in range(num_neighbors):
                neighbor_id = input(f"Podaj identyfikator sąsiada {j+1} dla wierzchołka {vertex['id']}: ")
                neighbor_vertex = next((v for v in graph if v['id'] == neighbor_id), None)
                if neighbor_vertex is not None:
                    vertex['neighbors'].append(neighbor_vertex)

        graph.append(vertex)

    return graph

graph = create_graph()
dfs(graph)

for u in graph:
    print(f"Wierzchołek {u['id']}: Czas wejścia: {u['time_entry']}, Czas wyjścia: {u['time_exit']}")
