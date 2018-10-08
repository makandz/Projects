info = []
t = 0

while True:
    info.append(input())
    if info[t] == "SCHOOL":
        break
    t += 1

for a in range(len(info) - 2, -1, -2):
    print("Turn ", end = "")
    if info[a] == "R":
        print("LEFT ", end = "")
    else:
        print("RIGHT ", end = "")
    if a == 0:
        print("into your HOME.")
    else:
        print("onto " + info[a - 1] + " street.")