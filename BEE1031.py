T = [[0 if i < 2 else -1 for _ in range(1001)] for i in range(101)]

def josephus(n, k):
    if T[n][k] == - 1:
        T[n][k] = (josephus(n - 1, k) + k) % n
    return T[n][k]


while True:
    try:
        n = int(input())

        if n == 0:
            break

        m = 1
        while((josephus(n - 1, m) + 1) % n != 12):
            m += 1

        print(m)
    except EOFError:
        break