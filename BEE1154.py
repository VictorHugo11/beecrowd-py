soma = 0
quantidade = 0

while True:
    n = int(input())

    if n < 0:
        break
    else:
        soma += n
        quantidade += 1
print(f'{soma / quantidade:.2f}')
