import sys
input = sys.stdin.readline

length = int(input())
amount = int(input())
clubs = [int(input()) for a in range(amount)]
l = [1000 for n in range(length + 1)]
l[0] = 0

for a in range(length):
    for b in clubs:
        t = [b + a, l[a] + 1]
        if t[0] <= length and l[t[0]] > t[1]:
            l[t[0]] = t[1]

if l[-1] != 1000:
    print "Roberta wins in", l[-1], "strokes."
else:
    print "Roberta acknowledges defeat."
