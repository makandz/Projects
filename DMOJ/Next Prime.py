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
    
number = int(input())
done = False

while done == False:
    if isnumprime(number) == True:
        done = True
        break
    number += 1
    
print(number)