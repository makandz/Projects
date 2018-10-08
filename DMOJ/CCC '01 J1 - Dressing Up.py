a = int(input()); c = 1
for b in range(a//2):
    print("*"*c + " "*((a*2)-(c*2)) + ("*"*c))
    c += 2
print("*"*(a*2))
for b in range(a//2):
    c -= 2
    print("*"*c + " "*((a*2)-(c*2)) + ("*"*c))