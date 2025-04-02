n = int(input())

t = list(map(int, input().split()))

menor = min(t)

algoz = t.index(menor) + 1

print(algoz)