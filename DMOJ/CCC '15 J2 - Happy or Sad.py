a = input()
b = a.count(":-)")
c = a.count(":-(")
if b > c:
    print("happy")
elif b < c:
    print("sad")
elif b == c and b > 0:
    print("unsure")
else:
    print("none")