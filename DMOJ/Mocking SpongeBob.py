amount = int(input())
sen = [0 for n in range(amount)]

for i in range(amount):
    sen[i] = list(input())
    cap = False
    for z in range(len(sen[i])):
        if sen[i][z].isalpha() == True:
            if cap == True:
                cap = False
                sen[i][z] = sen[i][z].upper()
            else:
                sen[i][z] = sen[i][z].lower()
                cap = True
                
for x in range(amount):
    print("".join(sen[x]))