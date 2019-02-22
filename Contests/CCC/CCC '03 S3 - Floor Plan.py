import sys
input = sys.stdin.readline

debug = False

squares = int(input())
rows = int(input())
columns = int(input())

obj = [list(input().rstrip("\n")) for a in range(rows)]
t_c = 0
used = 0
rooms = 0
sizes = []

if debug:
    for a in range(rows):
        print(obj[a])

def search(x, y):
    global t_c
    if x < 0 or x > (columns - 1) or y < 0 or y > (rows - 1) or obj[y][x] == "I":
        return
    else:
        t_c += 1
        obj[y][x] = "I"
    for z1, z2 in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        search(x + z1, y + z2)
        
for _y in range(rows):
    for _x in range(columns):
        if obj[_y][_x] == ".":
            search(_x, _y)
            if debug:
                print("Squares used this round:", t_c)
                if used + t_c < squares:
                    print("Current Square Use:", used + t_c)
            sizes.append(t_c)
            t_c = 0
            if debug:
                print("Found a room:", [_y, _x])
                for a in range(rows):
                    print(obj[a])

sizes.sort(reverse = True)
for a in range(len(sizes)):
    if used + sizes[a] <= squares:
        rooms += 1
        used += sizes[a]
    else:
        break

if rooms < 2:
    text = "room"
else:
    text = "rooms"
print(rooms, text + ",", (squares - used), "square metre(s) left over")