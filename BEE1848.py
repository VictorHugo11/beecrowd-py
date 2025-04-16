cont = 0
res = []

while cont < 3:
    s = 0 
    while True:
        l = input()
        if l == "caw caw":
            res.append(s)
            cont += 1
            break
        valor = 0
        if l[0] == "*":
            valor += 4
        if l[1] == "*":
            valor += 2
        if l[2] == "*":
            valor += 1
        s += valor
    
for resultado in res:
    print(resultado)