alice = input().split(" ")
bob = input().split(" ")
charlie = input().split(" ")

alice = [int(i) for i in alice]
bob = [int(i) for i in bob]
charlie = [int(i) for i in charlie]

dis = [(((bob[0] - alice[0])**2) + ((bob[1] - alice[1])**2)), (((charlie[0] - bob[0])**2) + ((charlie[1] - bob[1])**2)), (((charlie[0] - alice[0])**2) + ((charlie[1] - alice[1])**2))]

print(min(dis))