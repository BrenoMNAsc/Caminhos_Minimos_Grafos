import math
class Grafo:
    def __init__(self, qtd_vertices):
        self.qtd_vertices = qtd_vertices
        self.arestas = []

    def adicionar_aresta(self, origem, destino, peso):
        self.arestas.append((origem, destino, peso))

    def exibir_caminho(self, distancias):
        print(f"{':'}{'Vertices':>9}{':':>2}{'Distancia':>10}{':':>2}")
        for vertice in range(self.qtd_vertices):
            distancia = distancias[vertice]
            print(f"{':'}{str(vertice):>9}{':':>2}{str(distancia):>10}{':':>2}")

    def bellman_ford(self, origem):
        distancias = [math.inf] * self.qtd_vertices
        distancias[origem] = 0

        for _ in range(self.qtd_vertices - 1):
            for origem, destino, peso in self.arestas:
                if distancias[origem] != math.inf and distancias[origem] + peso < distancias[destino]:
                    distancias[destino] = distancias[origem] + peso

        for origem, destino, peso in self.arestas:
            if distancias[origem] != math.inf and distancias[origem] + peso < distancias[destino]:
                print("O grafo contém um ciclo de peso negativo")
                return

        self.exibir_caminho(distancias)