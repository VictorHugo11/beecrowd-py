while True:
    n = int(input())

    if n == 0:
        break
    
    matriz = [[0] *n for _ in range(n)]

    for b in range((n + 1 ) // 2):
        for i in range(b, n - b):
            for j in range(b, n - b):
                matriz[i][j] = b + 1

    for line in matriz:
        print(" ". join(f'{num:3}' for num in line))
    print()


