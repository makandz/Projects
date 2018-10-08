import math as m
s = [[0]*2 for n in range(10)]
# 0 is not
# 1 is red
b = 0
while True:
    v = input()
    if v == "red":
        s[b][0] += 1
    elif v == "end of box":
        t = 0
        t += s[b][0] * 16
        t += m.ceil(s[b][1] / 7) * 13
        print(t)
        b += 1
    else:
        s[b][1] += 1
    if b == 1:
        break

print(s)
#128 + 