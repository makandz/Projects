plan1 = 0
plan2 = 0

daytime = int(input())
even = int(input())
weekend = int(input())

if daytime > 100:
    plan1 = (daytime - 100) * 0.25

if daytime > 250:
    plan2 = (daytime - 250) * 0.25
    
if even > 0:
    plan1 += even * 0.15
    
if even > 0:
    plan2 += even * 0.35
    
if weekend > 0:
    plan1 += weekend * 0.2
    
if weekend > 0:
    plan2 += weekend * 0.25
    
print("Plan A costs " + str(round(plan1, 2)))
print("Plan B costs " + str(round(plan2, 2)))
if plan1 > plan2:
    print("Plan B is cheapest.")
elif plan1 < plan2:
    print("Plan A is cheapest.")
else:
    print("Plan A and B are the same price.")