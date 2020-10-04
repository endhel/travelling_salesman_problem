def nearest_neighbors(graph):
    u = 0
    c = []
    vertices = [i for i in range(len(graph))]
    vertices.remove(u)

    while len(vertices) != 0:
        minimum = float('inf')
        v = -1
        for i in range(len(graph)):
            if i not in c and graph[u][i] < minimum:
                minimum = graph[u][i]
                v = i
        c.append(v)
        if v != 0:
            vertices.remove(v)
        u = v
    c.append(c[0])
    return c

