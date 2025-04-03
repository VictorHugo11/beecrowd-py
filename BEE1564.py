import sys

for linha in sys.stdin:
    try:
        n = int(linha.strip())

        if n == 0:
            print('vai ter copa!')
        else:
            print('vai ter duas!')
    except EOFError:
        break