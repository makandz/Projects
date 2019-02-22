a = input()
b = input()
if b[-1] == "s":
    print(a + "-tu les", b, "?")
elif b[-1] == "e":
    print(a + "-tu la", b, "?")
else:
    print(a + "-tu le", b, "?")