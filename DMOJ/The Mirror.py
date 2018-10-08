import math

def isnumprime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

num = int(input())
lengths = [[0]*2 for n in range(num)]
amount = [0 for n in range(num)]
for a in range(num):
    lengths[a] = input().split(" ")
    for b in range(int(lengths[a][0]), int(lengths[a][1])):
        if isnumprime(b) == True:
            amount[a] += 1
    print(amount[a])