l = int(input())
s = int(input())
d = s - l
if d <= 0:
    print("Congratulations, you are within the speed limit!")
elif d >= 1 and d <= 20:
    print("You are speeding and your fine is $100.")
elif d >= 21 and d <= 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")