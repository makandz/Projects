debug = False

pages = int(input())
if debug:
    print("Pages:", pages)
    
obj = [0 for n in range(pages)]
for a in range(pages):
    obj[a] = list(map(int, input().split()))
    
if debug:
    print("Current Object:", obj)
  
q = [1, None]
s = []
possible = False
spath = 1
cur = 0
   
while True:
    if debug:
        print("Current queue:", q)
    qlen = len(q)
    if qlen > 0:
        cur = q.pop(0)
        if cur == None:
            if not possible:
                spath += 1
            if qlen > 1:
                q.append(None)
                if debug:
                    print("Added an end:", q)
            else:
                break
        else:
            s.append(cur)
            if obj[cur - 1][0] == 0:
                possible = True
                obj[cur - 1][0] = None
                if debug:
                    print("It's possible to end on page:", cur)
            else:
                if debug:
                    print("There are pages to go through:", obj[cur - 1][0])
                for b in range(1, obj[cur - 1][0] + 1):
                    if debug:
                        print("Adding page:", obj[cur - 1][b])
                    if (obj[cur - 1][b] not in q and obj[cur - 1][b] not in s) and obj[obj[cur - 1][b] - 1][0] != None:
                        q.append(obj[cur - 1][b])
                obj[cur - 1][0] = None
                if debug:
                    print("Set page as visited:", obj[cur - 1])
    else:
        break
    
if debug:
    print("Object:", obj)
    print("Solutions:", s, " and length of pages:", pages)
    print("Final Answer:")
if len(s) == pages:
    print("Y")
else:
    print("N")
if possible:
    print(spath)
else:
    print(0)