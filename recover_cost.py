def rec_cost(g, p):
    cost = 0
    for j in range(len(p)):
        if j == len(g):
            break
        cost += g[p[j]][p[j + 1]]
    return cost