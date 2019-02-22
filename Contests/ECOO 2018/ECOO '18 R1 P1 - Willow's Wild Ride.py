for a in range(10):
    cu = input()
    cu = list(map(int, cu.split(" ")))
    B = 0
    E = 0
    D = 0 # days left to finish using boxes
    for b in range(cu[1]):
        now = input()
        if now == "B":
            D += cu[0]
        if D > 0:
            D -= 1
    print(D)