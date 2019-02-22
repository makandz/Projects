import sys
input = sys.stdin.readline

cities = []
i = 0

while True:
    a = input().split()
    cities.append([int(a[1]), a[0]])
    if a[0] == "Waterloo":
        break
    i += 1

cities.sort()
print(cities[0][1])