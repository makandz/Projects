a = int(input("Enter max digits to count up to:"))
b = 0
c = 0
for i in range(1, a + 1):
    b += i**2
    c += i
print("Answer is " + str(c**2 - b))