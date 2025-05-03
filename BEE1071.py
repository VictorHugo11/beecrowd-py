a = int(input())
b = int(input())
start = min(a, b)+1
end = max(a, b)
if start % 2 == 0:
    start += 1
soma = 0
for i in range(start, end, 2):
    soma += i
print(soma)