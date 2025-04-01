import sys

for line in sys.stdin:
    n = int(line.strip())

    matriz = [['3' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        matriz[i][i] = '1'
        matriz[i][n - i - 1] = '2'
        
    for linha in matriz:
        print(''.join(linha))