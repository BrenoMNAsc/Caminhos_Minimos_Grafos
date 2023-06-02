from Grafo import Grafo

grafo = Grafo(11)
grafo.adicionar_aresta(0, 1, 4)
grafo.adicionar_aresta(0, 7, 8)
grafo.adicionar_aresta(1, 2, 8)
grafo.adicionar_aresta(1, 7, 11)
grafo.adicionar_aresta(2, 3, 7)
grafo.adicionar_aresta(2, 5, 4)
grafo.adicionar_aresta(6, 7, 1)
grafo.adicionar_aresta(6, 8, 6)
grafo.adicionar_aresta(7, 8, 7)
grafo.adicionar_aresta(9, 0, 2)
grafo.adicionar_aresta(10, 0, 4)

grafo.dijkstra(0)