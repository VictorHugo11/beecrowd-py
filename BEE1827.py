import sys

for linha in sys.stdin:
    try:
        n = int(linha.strip())

        matriz = [[0] * n for _ in range(n)]

        for i in range(n):
            matriz[i][i] = 2
            matriz[i][n - i - 1] = 3

        inicio = n // 3
        fim = n - inicio

        for i in range(inicio, fim):
            for j in range(inicio, fim):
                matriz[i][j] = 1

        matriz[n // 2 ][n //2 ] = 4

        for k in matriz:
            print("".join(map(str, k)))
        print("")
    except EOFError:
        break