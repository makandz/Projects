a = input().split(" ")
if a[len(a) - 1] == "False":
    a[len(a) - 1] = False
if (len(a) - 1) % 2 == 1:
    print(not bool(a[len(a) - 1]))
else:
    print(bool(a[len(a) - 1]))