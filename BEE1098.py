i = 0
j = 1
value = 0 
temp = 0 
temp2 = 0

while i <= 2:
    if temp2 == 0:
        print(f"I={i:.0f} J={j:.0f}")
    else:
        print(f"I={i:.1f} J={j:.1f}")
        
    temp += 1
    if temp == 3:
        i += 0.2
        value += 0.2
        j = value
        temp = 0
        temp2 += 1

    if temp2 == 5:
        temp2 = 0
    j += 1