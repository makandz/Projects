info = list(map(int, input().split(" ")))
obj = {n: [] for n in range(1, int(info[0]) + 1)}

for a in range(info[1]):
    val = list(map(int, input().split(" ")))
    if val[1] not in obj[val[0]]:
        obj[val[0]].append(val[1])
    if val[0] not in obj[val[1]]:
        obj[val[1]].append(val[0])
        
print(obj)

q = []
s = []
cur = info[2]
possible = False

if info[2] == info[3]:
    possible = True

while possible == False:
    for a in range(len(obj[cur])):
        if obj[cur][a] not in s and obj[cur][a] not in q:
            if obj[cur][a] == info[3]:
                possible = True
                break
                
            q.append(obj[cur][a])
    
    if possible == True:
        break
    elif len(q) > 0:
        cur = q[0]
        q.pop(0)
        s.append(cur)
    else:
        break
        
if possible:
    print("GO SHAHIR!")
else:
    print("NO SHAHIR!")