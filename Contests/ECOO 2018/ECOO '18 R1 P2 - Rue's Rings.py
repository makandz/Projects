for a in range(10):
    cu = int(input())
    roads = {}
    counter = [0 for n in range(cu)]
    imin = []
    for b in range(cu):
        N = list(map(int, input().split()))
        roads[N[0]] = N[2:]
        mi = min(N[2:])
        imin.append(mi)
        #print(mi)
    absmin = min(imin)
    print(absmin, end = " {")
    z = []
    for i in roads:
        if absmin in roads[i]:
            z.append(i)
    z.sort()
    for q in range(len(z)):
        if q + 1 == len(z):
            print(z[q], end = "")
        else:
            print(z[q], end = ",")
    print("}")

# for i in range (10):
#     # #
#     # N = M[0]
#     # for j in range(N):
#     #     a = M[j]
#     #     Z = a[0]
#     #     R = a[1]
#     #     D = copy.copy(a[2:])
#     #     D.sort()

        