import sys
input = sys.stdin.readline

for i in range(int(input())):
    found = False
    q = list(map(int, input().split()))
    if (q[2] / q[0] == q[2] // q[0] or q[2] / q[1] == q[2] // q[1]):
        print("YES")
    else:
        att = [q[0], q[1]]
        l = 2
        c = 0
        while True:
            lul = att[c]
            if lul < q[2]:
                z = lul + q[0]
                y = lul + q[1]
                if (z == q[2] or y == q[2]):
                    found = True
                    break
                if (z < q[2] and not z in att):
                    att.append(z)
                    l += 1
                if (y < q[2] and not y in att):
                    att.append(y)
                    l += 1
            c += 1
            if (c == l - 1):
                break
        if found:
            print("YES")
        else:
            print("NO")