total = 0
cur = 1

for i in range(3):
    temp = input()
    if temp == "":
        break
    else:
        total += int(temp) * cur
        if cur == 3:
            cur = 1
        else:
            cur = 3
            
print("The 1-3-sum is " + str(total + 91))