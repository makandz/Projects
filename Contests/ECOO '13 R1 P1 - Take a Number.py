c = int(input())
s = 0
w = 0

while True:
    t = input()
    if t == "TAKE":
        if c == 999:
            c = 0
        w += 1
        c += 1
    elif t == "SERVE":
        s += 1
        w -= 1
    elif t == "CLOSE":
        print(str(s + w), str(w), str(c))
        w = 0
        s = 0
    else:
        break