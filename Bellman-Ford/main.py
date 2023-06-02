from Grafo import Grafo

grafo = Grafo(6)
grafo.adicionar_aresta(0, 1, -1)
grafo.adicionar_aresta(0, 2, 4)
grafo.adicionar_aresta(1, 2, 3)
grafo.adicionar_aresta(1, 3, 2)
grafo.adicionar_aresta(1, 4, 2)
grafo.adicionar_aresta(3, 2, 5)
grafo.adicionar_aresta(3, 1, 1)
grafo.adicionar_aresta(4, 3, -3)
grafo.adicionar_aresta(5, 0, 3)

grafo.bellman_ford(0)