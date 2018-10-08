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

print("All primes for", number, "are:")

z = 0

for a in range(number):
    b = a + 1
    if isnumprime(b):
        z += 1
        
print(z)