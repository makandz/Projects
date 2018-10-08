start = int(input(""))
stop = int(input(""))

amount = 0

def opp(val):
    if val == 0 or val == 1 or val == 8:
        return val
    elif val == 6:
        return 9
    elif val == 9:
        return 6
    else:
        return False

for i in range(start, stop + 1):
    strdig = str(i)
    length = len(strdig)
    failed = False
    oppo = [0 for n in range(length)]
    for x in range(length - 1, -1, -1):
        temp = opp(int(strdig[x]))
        if type(temp) == type(False):
            failed = True
        else:
            oppo[length - 1 - x] = str(temp)
    if failed == False and "".join(oppo) == strdig:
        print(strdig)
        amount += 1
        
print(str(amount))