w = float(input())
h = float(input())
b = w/(h*h)
if b > 25:
    print("Overweight")
elif b < 18.5:
    print("Underweight")
else:
    print("Normal weight")