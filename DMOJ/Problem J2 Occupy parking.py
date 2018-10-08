amount = int(input(""))
yes = list(input(""))
tod = list(input(""))
taken = 0

for a in range(amount):
    if tod[a] == yes[a] and tod[a] == "C":
        taken += 1
        
print(taken)