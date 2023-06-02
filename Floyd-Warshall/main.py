from Grafo import Grafo

grafo = Grafo(4)
grafo.adicionar_aresta(0, 1, 3)
grafo.adicionar_aresta(0, 3, 7)
grafo.adicionar_aresta(1, 0, 2)
grafo.adicionar_aresta(1, 2, 1)
grafo.adicionar_aresta(2, 3, 2)

grafo.floyd_warshall()