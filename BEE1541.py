import math

while True:
    try:
        entrada = input().strip()

        if entrada == '0':
            break

        a, b, c = map(int, entrada.split())

        ac = a * b
        at = ac / (c / 100)
        lt = int(math.sqrt(at))

        print(lt)

    except EOFError:
        break