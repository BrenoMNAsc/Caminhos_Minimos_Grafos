import heapq
import math

def main():
    grafo = {1: {1: 0, 2: 10, 3: 5, 4: math.inf, 5: math.inf},
             2: {1: math.inf, 2: 0, 3: 2, 4: 1, 5: math.inf},
             3: {1: math.inf, 2: 3, 3: 0, 4: 9, 5: 2},
             4: {1: math.inf, 2: math.inf, 3: math.inf, 4: 0, 5: 4},
             5: {1: 7, 2: math.inf, 3: math.inf, 4: 6, 5: 0}}
    c = Dijkstra(grafo, 1)
    exibir_matriz_caminhos(c, 1)


def Dijkstra(grafo, v):
    c = {v:0}
    for i in range(2, len(grafo) +1):
        c.update({i:grafo[v][i]})
    heap = [(c[i], i) for i in range(1,len(grafo) +1)]
    heapq.heapify(heap)
    while heap:
        (custo, w) = heapq.heappop(heap)
        N = Ns_Vizinho(grafo, w, heap)
        for (cuzto, z) in N:
            if c[w] + grafo[w][z] < c[z]:
                c[z] = c[w] + grafo[w][z]
                for i in range(len(heap)):
                    if (heap[i][1] == z):
                        heap[i] = (c[z], z)
                        heapq.heapify(heap)
    return c



def Ns_Vizinho(grafo, w, heap):
    N = []
    for z in grafo[w]:
        if grafo[w][z] != math.inf:
            for j in heap:
                if (z == j[1]):
                    N.append((grafo[w][z], z))
    return N

def exibir_matriz_caminhos(c,v):
    print("Caminhos")
    for i in range(1,len(c) +1):
        print(f"[{v}]--{c[i]}-->[{i}]")

if __name__ == "__main__":
    main()