import math

data = input("")
info = data.split(" ")

weeks = math.ceil((int(info[1]) + int(info[0]) - 1) / 7)

first = True
current = 1
days = [[0]*7 for n in range(weeks)]

for x in range(0, weeks):
    for z in range(1, 8):
        if current > int(info[1]):
            break
        
        if first:
            if z != int(info[0]):
                days[x][z - 1] = " "
            else:
                days[x][z - 1] = str(current)
                current += 1
                first = False
        else:
            days[x][z - 1] = str(current)
            current += 1

print("Sun Mon Tue Wed Thr Fri Sat")
for x in range(0, len(days)):
    lendays = len(days[x])
    
    for z in range(0, lendays):
        if days[x][z] == 0:
            break
        elif z == 0:
            start = ""
        else:
            start = " "
        
        if len(str(days[x][z])) == 2:
            print(" " + start + str(days[x][z]), end = "")
        else:
            print("  " + start + str(days[x][z]), end = "")
    print("", end = "\n")