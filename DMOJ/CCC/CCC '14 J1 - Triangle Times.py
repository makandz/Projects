ang1 = int(input(""))
ang2 = int(input(""))
ang3 = int(input(""))

total = ang1 + ang2 + ang3

tri = 0

if total != 180:
    tri = 0
elif ang1 == 60 and ang2 == 60 and ang3 == 60:
    tri = 1
elif ang1 == ang2 or ang2 == ang3 or ang1 == ang3:
    tri = 2
else:
    tri = 3
    
if tri == 1:
    print("Equilateral")
elif tri == 2:
    print("Isosceles")
elif tri == 3:
    print("Scalene")
else:
    print("Error")