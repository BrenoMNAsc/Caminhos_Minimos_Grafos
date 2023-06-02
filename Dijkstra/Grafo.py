import math
import heapq

class Grafo:
    def __init__(self, qtd_vertices):
        self.qtd_vertices = qtd_vertices
        self.adjacencias = [[] for i in range(qtd_vertices)]

    def adicionar_aresta(self, origem, destino, peso):
        if(peso < 0):
            print("Peso não pode ser negativo")
            return
        else:
            self.adjacencias[origem].append((destino, peso))

    def exibir_caminho(self, distancias):
        print(f"{':'}{'Vertices':>9}{':':>2}{'Distancia':>10}{':':>2}")
        for vertice in range(self.qtd_vertices):
            distancia = distancias[vertice]
            print(f"{':'}{str(vertice):>9}{':':>2}{str(distancia):>10}{':':>2}")

    def dijkstra(self, origem):
        distancias = [math.inf] * self.qtd_vertices
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