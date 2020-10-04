from itertools import permutations
from recover_cost import rec_cost


def brute_force(graph):
    cost_min = float('inf')
    c_best = []
    for c in permutations(range(len(graph)), len(graph)):
        aux = list(c)
        aux.append(c[0])
        c = aux
        cost_c = rec_cost(graph, c)
        if cost_min > cost_c:
            cost_min = cost_c
            c_best = c
    return c_best
