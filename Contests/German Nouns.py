a = int(input())
for z in range(a):
    w = input().split(" ")
    b = 0
    for x in range(len(w)):
        if w[x].lower() != w[x]:
            b += 1
    print(b)