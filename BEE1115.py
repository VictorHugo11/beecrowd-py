x, y = map(int, input().split())

while True:
    if x > 0 and y > 0:
        print('primeiro')
    elif x < 0 and y > 0:
        print('segundo')
    elif x < 0 and y < 0:
        print('terceiro')
    elif x > 0 and y < 0:
        print('quarto')
    else:
        break
    x, y = map(int, input().split())