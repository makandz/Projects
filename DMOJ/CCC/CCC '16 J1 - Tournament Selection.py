w = 0
for a in range(6):
    if input() == "W":
        w += 1
if w == 1 or w == 2:
    print(3)
elif w == 3 or w == 4:
    print(2)
elif w == 5 or w == 6:
    print(1)
else:
    print(-1)