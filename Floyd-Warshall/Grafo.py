import sys

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacencias = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, origem, destino, peso):
        self.adjacencias[origem].append((destino, peso))

    def exibir_caminho(self, distancias):
        print("Distancias entre os vertices:")
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                distancia = distancias[i][j]
                if distancia == sys.maxsize:
                    distancia = "∞"
                print(f"De {i} para {j}: {distancia}")

    def floyd_warshall(self):
        distancias = [[sys.maxsize] * self.num_vertices for _ in range(self.num_vertices)]

        for v in range(self.num_vertices):
            distancias[v][v] = 0

            for vizinho, peso in self.adjacencias[v]:
                distancias[v][vizinho] = peso

        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

        self.exibir_caminho(distancias)