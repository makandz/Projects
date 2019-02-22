q = int(input(""))
s1 = int(input(""))
s2 = int(input(""))
s3 = int(input(""))

s1 = s1 - ((s1 // 35) * 35)
s2 = s2 - ((s2 // 100) * 100)
s3 = s3 - ((s3 // 10) * 10)

a = 0

while q > 0:
    s1 += 1
    if s1 == 35:
        s1 = 0
        q += 30
    
    q -= 1
    
    if q == 0:
        a += 1
        break
    
    s2 += 1
    if s2 == 100:
        s2 = 0
        q += 60
        
    q -= 1
        
    if q == 0:
        a += 2
        break
    
    s3 += 1
    if s3 == 10:
        s3 = 0
        q += 9
        
    q -= 1
    a += 3
    
print("Martha plays " + str(a) + " times before going broke.")