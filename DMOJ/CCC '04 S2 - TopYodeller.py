import sys
input = sys.stdin.readline

N, R = map(int, input().split())
Y = [[0, a] for a in range(N)] # total, index
H = [[0 for n in range(R)] for b in range(N)]

for c in range(R):
    S = list(map(int, input().split()))
    for i in range(N):
        Y[i][0] += S[i]
    Q = Y[:]
    Q.sort(reverse = True)
    RA = -1
    for i in range(N):
        if (c != R - 1):
            if (i != 0) and (Q[i][0] == Q[i - 1][0]):
                H[Q[i][1]][c] = RA
            else:
                RA += 1
                H[Q[i][1]][c] = RA

Q.sort(key = lambda k: (k[0], -k[1]), reverse = True)
Z = Q[0][0]
for a in range(N):
    if Q[a][0] == Z:
        print("Yodeller", Q[a][1] + 1, "is the TopYodeller: score", str(Q[a][0]) + ", worst rank", max(H[Q[a][1]]) + 1)