while True:

    k = int(input())

    if k == 0:
        break

    n, m = map(int, input().split()) #leste-oeste

    for i in range(k):
        x, y = map(int, input().split()) # norte-sul

        if x == n or y == m:
            print("divisa")
        elif x > n and y > m:
            print("NE")
        elif x < n and y > m:
            print("NO")
        elif x < n and y < m:
            print("SO")
        elif x > n and y < m:
            print("SE")