info = input().split(" ")
info = [int(i) for i in info]
strokes = [[0]*2 for n in range(info[1])]
strip = [0 for n in range(info[0])]

for a in range(info[1]):
    strokes[a] = input().split(" ")
    
blue = strip.count(1)

print(str(info[0] - blue) + " " + str(blue))