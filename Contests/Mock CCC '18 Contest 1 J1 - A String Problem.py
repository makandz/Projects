num = int(input(""))
binary = str("{0:b}".format(num))

binarys = list(binary)
binr = ""

for a in range(len(binarys)):
    if (binarys[a] == "0"):
        binarys[a] = "1"
    binr += str(binarys[a])

print(int(binr, 2))