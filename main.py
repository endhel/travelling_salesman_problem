from create_graph import create_graph
from time import time
from nearest_neighbors import nearest_neighbors
from brute_force import brute_force
from recover_cost import rec_cost


print('Grafo:')
graph = create_graph(5, 1, 9)

for i in range(len(graph)):
    print(graph[i])
print()

option = int(input("Algoritmo: \n\t1 Guloso\n\t2 Forca Bruta\n"))

print()
print('Processando...')
print()

inicio = time()
if option == 1:
    path = nearest_neighbors(graph)
    fim = time()
    print(f'Caminho: {path}')
    print(f'Custo do Caminho: {rec_cost(graph, path)}')
    print(f'Tempo: {fim - inicio}')
if option == 2:
    path = brute_force(graph)
    fim = time()
    print(f'Caminho: {path}')
    print(f'Custo do Caminho: {rec_cost(graph, path)}')
    print(f'Tempo: {fim - inicio}')
