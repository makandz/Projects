t = int(input())
s = int(input())
h = int(input())
def space(c):
    for d in range(c):
        print(" ", end = "")
for a in range(t):
    print("*", end = "")
    space(s)
    print("*", end = "")
    space(s)
    print("*")
for e in range((s + 1) * 2):
    print("*", end = "")
print("*")
for f in range(h):
    space(s + 1)
    print("*", end = "")
    space(s + 1)
    print("")