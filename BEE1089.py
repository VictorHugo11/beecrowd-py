while True:

    n = int(input())
    
    if n == 0:
        break
    
    h = list(map(int, input().split()))

    picos = 0

    for i in range(n):
        prev = (i - 1) % n
        next = (i + 1) % n

        if h[i] > h[prev] and h[i] > h[next]:
            picos += 1
        elif h[i] < h[prev] and h[i] < h[next]:
            picos += 1

    print(picos)

        
        
