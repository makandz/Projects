input = __import__("sys").stdin.readline

W, H, N = map(int, input().split())

xd = []
xd.append([0] * (W + 1)) #dumb

for r in range(1, H + 1):
    xd.append([0] + list(map(int, input().split())))

def sum(r1, c1, r2, c2):
    return xd[r2][c2] - xd[r2][c1 - 1] - xd[r1 - 1][c2] + xd[r1 - 1][c1 - 1]

for r in range(1, H + 1):
    for c in range(1, W + 1):
        xd[r][c] += xd[r - 1][c] + xd[r][c - 1] - xd[r - 1][c - 1]

ans = 0
for height in range(1, H + 1):
    width = min(W, int(N / height))
    for r in range(height, H + 1):
        for c in range(1, W + 1):
            ans = max(ans, sum(r - height + 1, c - width + 1, r, c))

print(ans)