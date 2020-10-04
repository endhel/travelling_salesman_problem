from random import randint


def create_graph(num_vertices, min_weight, max_weight):
    graph = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(num_vertices - 1):
            if i == j:
                continue
            if graph[i][j] == 0:
                weight = randint(min_weight, max_weight)
                graph[i][j] = graph[j][i] = weight
    return graph
