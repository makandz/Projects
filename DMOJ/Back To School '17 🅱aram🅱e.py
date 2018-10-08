a = list(input())
for b in range(len(a)):
    if a[b].upper():
        a.insert(b - 1, ".")
print(str(a))