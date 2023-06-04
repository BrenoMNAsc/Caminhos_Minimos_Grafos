import math

def main():
    grafo = {
        1: {1: 0, 2: 1, 3: 2, 4: math.inf},
        2: {1: math.inf, 2: 0, 3: 3, 4: -1},
        3: {1: math.inf, 2: math.inf, 3: 0, 4: -2},
        4: {1: math.inf, 2: 2, 3: math.inf, 4: 0},
    }
    matrizes_c = Floyd_Warshall(grafo, 1)
    print_matrizes_caminhos(matrizes_c)


def Floyd_Warshall(grafo, v):
    c = grafo
    matriz_c = []
    matriz_c.append(c.copy())

    for k in range(1, len(grafo) + 1):
        aux = {}
        for i in range(1, len(grafo) + 1):
            aux[i] = {}
            for j in range(1, len(grafo) + 1):
                aux[i][j] = min(matriz_c[k - 1][i][j], matriz_c[k - 1][i][k] + matriz_c[k - 1][k][j])
        matriz_c.append(aux)

    return matriz_c


def print_matrizes_caminhos(matrizes_c):
    for k in range(len(matrizes_c)):
        print(f"Matriz C{k}:")
        for i in sorted(matrizes_c[k].keys()):
            for j in sorted(matrizes_c[k][i].keys()):
                print(f"{matrizes_c[k][i][j]:5}", end=" ")
            print()
        print()


if __name__ == "__main__":
    main()
