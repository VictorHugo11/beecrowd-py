def josephus(n, k):
    result = 0  
    for i in range(2, n + 1):
        result = (result + k) % i
    return result

while True:
    try:
        n = int(input())
        if n == 0:
            break

        m = 1
        while ((josephus(n - 1, m) + 1) % n != 12):
            m += 1

        print(m)
    except EOFError:
        break