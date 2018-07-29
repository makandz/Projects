DEBUG = True

def parseInt(s, f, v):
    if type(s) == float:
        if s.is_integer():
            s = int(s)
        else:
            return "wop"
    if f == "m": # Multiply
        return s * v[0]
    elif f == "s": # Subtract
        return s - v[0]
    elif f == "a": # Add
        return s + v[0]
    elif f == "d": # Divide
        return s / v[0]
    elif f == "e": # Exponent
        return s ** v[0]
    elif f == "f": # Flip Sign
        return s * -1
    elif f == "i": # Include Digit
        return int(str(s) + str(v[0]))
    elif f == "r": # Remove digit
        return s // 10
    elif f == "c": # Change Sign
        return int(str(s).replace(str(v[0]), str(v[1])))
    elif f == "n": # Flip Number
        if s > 0:
            return int(str(s)[::-1])
        else:
            return s
    else:
        return 0

st = int(input("Start:"))
g = int(input("Goal:"))
n = int(input("Amount of Functions:"))
c = [[0] for a in range(n)]
for b in range(n):
    a = input("Number " + str(b) + ":").split()
    c[b][0] = a.pop(0)
    c[b].append(list(map(int, a)))
if DEBUG:
    print("Working with:", c)

q = [parseInt(st, c[z][0], c[z][1]) for z in range(n)]
stp = [[c[z]] for z in range(n)]
if DEBUG:
    print("Current queue", q)
    print("Current steps", stp)

cn = False
sc = -1

while len(stp[len(stp) - 1]) < 10:
    cn = q.pop(0)
    sc += 1
    if cn == g:
        print("-------------------------------------------")
        print(":: Reached goal of", g, "in", len(stp[sc]), "steps!")
        print(":: Steps required:", stp[sc])
        break
    for b in range(n):
        z = stp[sc][:]
        z.append(c[b])
        y = parseInt(cn, c[b][0], c[b][1])
        if y != "wop":
            q.append(y)
            stp.append(z)
            if DEBUG:
                print("Queue updated:", q)
        else:
            if DEBUG:
                print("Queue was not updated..")
print(":: Script Stopped")
