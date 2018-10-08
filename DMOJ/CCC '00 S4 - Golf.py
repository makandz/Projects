import sys
input = sys.stdin.readline

DEBUG = False

length = int(input())
amount = int(input())
clubs = [int(input()) for a in range(amount)]
q = clubs[:]
q.append(None)
c = 1
al = []

def addnextsum(p):
    if DEBUG:
        print q
    for a in range(amount):
        np = p + clubs[a]
        if np == length:
            return True
        elif not np in al and np <= length:
            q.append(np)
            al.append(np)
    return False

while True:
    on = q.pop(0)
    if on == length:
        break
    elif on == None:
        if len(q) > 1:
            c += 1
            q.append(None)
        else:
            c = -1
            break
    else:
        if addnextsum(on):
            c += 1
            break

if c > 0:
    print "Roberta wins in", c, "strokes."
else:
    print "Roberta acknowledges defeat."