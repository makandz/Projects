amount = int(input())

for i in range(amount):
    binary = "{0:b}".format(int(input()))
    length = len(binary)
    count = 0
    mod = (length % 4)
    
    if mod != 0:
        for a in range(4 - (length % 4)):
            print("0", end = "")
            count += 1
        
    for a in range(length):
        count += 1
        if (count == 4 and a != length - 1):
            count = 0
            print(binary[a], end = " ")
        else:
            print(binary[a], end = "")
    print("")