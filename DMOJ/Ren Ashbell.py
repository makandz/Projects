a = int(input())
c = int(input())
s = True
for b in range(a - 1):
    if int(input()) >= c:
        s = False
if s:
    print("YES")
else:
    print("NO")