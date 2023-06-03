import heapq
import math

def main():
    grafo = {1: {1: 0, 2: 10, 3: 5, 4: math.inf, 5: math.inf},
             2: {1: math.inf, 2: 0, 3: 2, 4: -7, 5: math.inf},
             3: {1: math.inf, 2: 3, 3: 0, 4: 9, 5: -2},
             4: {1: math.inf, 2: math.inf, 3: math.inf, 4: 0, 5: 4},
             5: {1: 7, 2: math.inf, 3: math.inf, 4: 6, 5: 0}}
    c = Dijkstra(grafo, 1)
    exibir_matriz_caminhos(c)


def Dijkstra(grafo, v):
    c = []
    for i in range(2, len(grafo) + 1):
        c.append(grafo[v][i])
    c[v] = 0
    heap = []
    heapq.heappush(heap, (0 ,v))
    while heap:
        peso, vertice = heapq.heappop(heap)
        for vizinho, pesoAresta in grafo[vertice].items():
            novoPeso = c[vertice] + pesoAresta
            if novoPeso < c[vizinho]:
                c[vizinho] = novoPeso
                heapq.heappush(heap, (novoPeso, vizinho))

    return c

def exibir_matriz_caminhos(c):
    for l in sorted(c.keys()):
        for v in sorted(c[l].keys()):
            print(f"{c[l][v]:5}", end=" ")
        print()

if __name__ == "__main__":
    main()