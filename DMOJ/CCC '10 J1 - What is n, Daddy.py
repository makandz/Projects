n = int(input())

if n == 1 or n == 9 or n == 10:
    ways = 1
elif n == 2 or n == 3 or n == 8 or n == 7:
    ways = 2
else:
    ways = 3
    
print(ways)