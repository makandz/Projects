for a in range(10):
    au = list(map(int, input().split()))
    OUR = []
    FAIL = []
    # case 1
    for b in range(au[0]):
        number = list(input())
        number = list(map(int, number))
        for i in range(len(number)):
            if number[i] == 0:
                number[i] = au[3]
            elif number[i] % 2 == 1:
                if number[i] - au[2] > 0:
                    number[i] -= au[2]
                else:
                    number[i] = 0
            else:
                number[i] += au[1]
        temp = ""
        for z in number:
            temp += str(z)
        OUR.append(temp)

    input()

    # correct case
    for d in range(au[0]):
        if OUR[d] != input():
            FAIL.append(d + 1)

    if len(FAIL) > 0:
        print("FAIL: ", end = "")
        for q in range(len(FAIL)):
            if q == len(FAIL) - 1:
                print(FAIL[q])
            else:
                print(FAIL[q], end = ",")
    else:
        print("MATCH")
    
    input()