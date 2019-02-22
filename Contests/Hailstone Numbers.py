a = int(input())
b = 0
while True:
    if a == 1:
        break
    if a % 2 == 0:
        a /= 2
    else:
        a = (a * 3) + 1
    b += 1
print(b)