y_a = [2, 2, -2, -2, -1, -1, 1, 1]
x_a = [1, -1, 1, -1, 2, -2, 2, -2]
s = []

start = list(map(int, input().split()))
stop = list(map(int, input().split()))
print("Start Position", start)
print("End Position", stop)

q = [start, None]
c = 0

def add_8_paths(p):
    for a in range(8):
        np = [p[0] + x_a[a], p[1] + y_a[a]]
        if np not in q and np not in s and np[0] > 0 and np[1] > 0:
            q.append(np)

while True: # i actually should just use true
    on = q.pop(0)
    s.append(on)
    print("Currently on", on)
    if on == stop:
        print("Found it!")
        break
    elif on == None:
        c += 1
        q.append(None)
        print("Current Possible Queue", q)
    else:
        add_8_paths(on)
        
print(c)