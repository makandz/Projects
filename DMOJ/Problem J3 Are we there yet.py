import math

d = input("").split(" ")
n = 5

dis = [0 for n in range(5)]

d.insert(0, 0)

def show():
    for z in range(5):
        if z == 4:
            print(int(math.fabs(dis[z])))
        else:
            print(int(math.fabs(dis[z])), end = " ")
            
for i in range(5):
    for x in range(i + 1):
        dis[i] += int(d[x])

show()

location = 1
for a in range(4):
    for b in range(5):
        dis[b] -= int(d[location])
    show()
    location += 1