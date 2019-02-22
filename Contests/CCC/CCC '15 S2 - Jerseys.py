import sys
input = sys.stdin.readline

sizes = {"S": 1, "M": 2, "L": 3}

jers = int(input())
athl = int(input())
stuff = [input().rstrip() for n in range(jers)]

works = 0

for _ in range(athl):
    s = input().split()
    s[1] = int(s[1]) - 1
    if (stuff[s[1]] != 0 and sizes[stuff[s[1]]] >= sizes[s[0]]):
        works += 1
        stuff[s[1]] = 0

print(works)