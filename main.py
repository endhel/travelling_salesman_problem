from create_graph import create_graph
from time import time


print('Grafo:')
graph = create_graph(5, 1, 9)
for i in range(len(graph)):
    print(graph[i])
print()

option = int(input("Algoritmo: \n\t1 Guloso\n\t2 Forca Bruta"))

print()
print('Processando...')
print()

inicio = time()
if option == 1:
    print('Caminho: ')
    print(f'Custo do Caminho:')
    fim = time()
    print(f'Tempo: {fim - inicio}')
if option == 2:
    print('Caminho: ')
    print(f'Custo do Caminho:')
    fim = time()
    print(f'Tempo: {fim - inicio}')
if option == 3:
    print('\nCaminho:')
    print(f'Custo do Caminho:')
    fim = time()
    print(f'Tempo: {fim - inicio}')