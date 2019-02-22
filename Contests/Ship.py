p = list(input())
c = {"B": 0, "F": 0, "T": 0, "L": 0, "C": 0}
for a in range(len(p)):
    c[p[a]] = 1
m = False
for b in c:
    if c[b] == 0:
        print(b)
        m = True
if m == False:
    print("NO MISSING PARTS")