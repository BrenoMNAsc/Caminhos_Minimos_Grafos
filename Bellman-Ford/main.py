import math


def main():
    grafo = {1: {1: 0, 2: 10, 3: 5, 4: math.inf, 5: math.inf},
             2: {1: math.inf, 2: 0, 3: 2, 4: -7, 5:math.inf},
             3: {1: math.inf, 2: 3, 3: 0, 4: 9, 5:-2},
             4: {1: math.inf, 2: math.inf, 3: math.inf, 4: 0, 5: 4},
             5: {1:7, 2:math.inf, 3:math.inf, 4:6, 5:0}}
    c = Bellman_Ford(grafo)
    exibir_matriz_caminhos(c)


def Bellman_Ford(grafo):
    c = {0: {1: 0}}
    for i in range(2, len(grafo) + 1):
        c[0][i] = math.inf

    for l in range(1, len(grafo)):
        for k in range(1, len(grafo) + 1):
            c[l] = c.get(l, {})
            c[l][k] = min(c[l-1][k],Menor_dis_vizinhoP(grafo, c, l, k))

    return c


def Menor_dis_vizinhoP(grafo, c, l, k):
    menorDis = math.inf
    for v in range(1, len(grafo) + 1):
        if grafo[v][k] != math.inf:
            if menorDis > c.get(l - 1, {}).get(v, math.inf) + grafo[v][k]:
                menorDis = c.get(l - 1, {}).get(v, math.inf) + grafo[v][k]
    return menorDis

def exibir_matriz_caminhos(c):
    for l in sorted(c.keys()):
        for v in sorted(c[l].keys()):
            print(f"{c[l][v]:5}", end=" ")
        print()

if __name__ == "__main__":
    main()