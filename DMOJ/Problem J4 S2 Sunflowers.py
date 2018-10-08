length = int(input())
array = [input().split(" ") for n in range(length)]
for a in range(length):
    array[a] = [int(array[a][i]) for i in range(length)]

def rotate():
    temp = [[0]*length for n in range(length)]
    for y in range(length):
        for x in range(length):
            temp[length - 1 - x][y] = array[y][x]
    return temp
    
largest = 0
done = False
while done == False:
    for y in range(length):
        failed = False
        largestx = 0
        for x in range(length):
            if largestx <= array[y][x]:
                largestx = array[y][x]
            else:
                failed = True
                break
        if failed == True:
            break
        
        if largest <= array[y][length - 1] and y == length - 1:
            done = True
            break
        elif largest <= array[y][length - 1]:
            largest = array[y][length - 1]
            
    if done == False:
        array = rotate()

for y in range(length):
    for x in range(length):
        if x == length - 1:
            _end = "\n"
        else:
            _end = " "
        print(array[y][x], end = _end)