num = [0 for n in range(4)]

for i in range(4):
    num[i] = int(input(""))

failed = False

if (num[0] == 8 or num[0] == 9) and (num[3] == 8 or num[3] == 9) and (num[1] == num[2]):
    print("ignore")
else:
    print("answer")