from decimal import Decimal, ROUND_HALF_UP
m = [int(input()) for a in range(3)]
r = (m[1] - round(float(Decimal(Decimal((m[0] * (1 - (m[2] / 100)))).quantize(Decimal('.1'), rounding = ROUND_HALF_UP))))) / (m[2] / 100)
if r > 100:
    print("DROP THE COURSE")
else:
    if r > 0:
        print(Decimal(r).quantize(0, ROUND_HALF_UP))
    else:
        print(0)