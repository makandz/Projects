import sys
input = sys.stdin.readline
a = list(map(int, input().split()))
c = 0
for b in range(a[0]):
    i = list(map(int, input().split()))
    if (i[0] * (1 - (i[1] / 100))) <= a[1]:
        c += 1
print(c)