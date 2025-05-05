n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    if a > b:
        a, b = b, a
    
    soma_impares = 0

    for num in range(a + 1, b):
        if num % 2 != 0:  # verifica se é ímpar
            soma_impares += num

    print(soma_impares)
