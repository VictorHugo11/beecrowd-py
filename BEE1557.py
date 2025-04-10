while True:
    n = int(input())

    if n == 0:
        break
    
    matriz = [[0] * n for _ in range(n)]

    T = len(str(2 ** (2 * (n - 1))))

    for i in range(n):
        for j in range(n):
            matriz[i][j] = 2 ** (i + j)

    for line in matriz:
        print(" ".join(f"{num:>{T}}" for num in line))
    print()
