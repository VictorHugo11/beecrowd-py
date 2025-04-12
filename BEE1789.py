while True:
    try:
        n = int(input())
        a = list(map(int, input().split()))
        maior = max(a)
        
        if maior < 10:
            print("1")

        if maior >= 10 and maior < 20:
            print("2")

        if maior >= 20:

            print("3")

    except EOFError:
        break