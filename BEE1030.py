def josephus(n, k):
    pos = 0 
    for i in range(2, n + 1):
        pos = (pos + k) % i
    return pos + 1
    
a = int(input())

for case in range(1, a + 1):
    n, k = map(int, input().split())
    sobra = josephus(n, k)
    print(f"Case {case}: {sobra}")
