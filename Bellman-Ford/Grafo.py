import math
class Grafo:
    def __init__(self, qtd_vertices):
        self.qtd_vertices = qtd_vertices
        self.arestas = []

    def adicionarAresta(self, origem, destino, peso):
        self.arestas.append((origem, destino, peso))

    def exibirCaminho(self, distancias):
        print(f"{':'}{'Vertices':>9}{':':>2}{'Distancia':>10}{':':>2}")
        for vertice in range(self.qtd_vertices):
            distancia = distancias[vertice]
            print(f"{':'}{str(vertice):>9}{':':>2}{str(distancia):>10}{':':>2}")

    def bellman_ford(self, origem):
        distancias = []
        distancias[origem] = 0
        for i in range(self.qtd_vertices - 1):
            for origem, destino, peso in self.arestas:
                if distancias[origem] != math.inf and distancias[origem] + peso < distancias[destino]:
                    distancias[destino] = distancias[origem] + peso
        for origem, destino, peso in self.arestas:
            if distancias[origem] != math.inf and distancias[origem] + peso < distancias[destino]:
                print("Este grafo possui ciclos negativos")
                return
        self.exibirCaminho(distancias)