bowls = [0 for n in range(3)]
for a in range(3):
    bowls[a] = int(input())
bowls.sort()
print(bowls[1])