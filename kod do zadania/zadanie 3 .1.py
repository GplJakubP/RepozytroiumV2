from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        print(vertex)

        if vertex not in visited:
            visited.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

def create_graph(num_vertices):
    graph = {}
    for i in range(num_vertices):
        vertex = str(i)
        connections = input(f"Podaj połączenia dla wierzchołka {vertex} (oddzielone spacjami): ").split()
        graph[vertex] = connections
    return graph

num_vertices = int(input("Podaj liczbę wierzchołków w grafie: "))
graph = create_graph(num_vertices)
start_vertex = input("Podaj numer wierzchołka startowego: ")

bfs(graph, start_vertex)
