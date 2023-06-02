import sys
import heapq

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacencias = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, origem, destino, peso):
        self.adjacencias[origem].append((destino, peso))

    def exibir_caminho(self, distancias):
        print("Vertice \tDistancia do vertice de origem")
        for node in range(self.num_vertices):
            distancia = distancias[node]
            if distancia == sys.maxsize:
                distancia = "∞"
            print(f"{node} \t\t{distancia}")

    def dijkstra(self, origem):
        distancias = [sys.maxsize] * self.num_vertices
        distancias[origem] = 0

        fila = [(0, origem)]

        while fila:
            dist, atual = heapq.heappop(fila)

            if dist > distancias[atual]:
                continue

            for vizinho, peso in self.adjacencias[atual]:
                nova_dist = dist + peso

                if nova_dist < distancias[vizinho]:
                    distancias[vizinho] = nova_dist
                    heapq.heappush(fila, (nova_dist, vizinho))

        self.exibir_caminho(distancias)