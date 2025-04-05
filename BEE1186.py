c = input().upper()
matriz = []

for _ in range(12 * 12):
    matriz.append(float(input()))

soma = 0
cont = 0

for i in range(12):
    for j in range(12):
        if i + j > 11:
            soma += matriz[i * 12 + j]
            cont += 1
            
if c == "S":
    print(f"{soma:.1f}")

elif c == "M":
    print(f"{soma / cont:.1f}")
