# I have no idea if this is actually functioning.

def line_intersection(l1, l2):
    xdiff = (l1[0][0] - l1[1][0], l2[0][0] - l2[1][0])
    ydiff = (l1[0][1] - l1[1][1], l2[0][1] - l2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return False

    d = (det(*l1), det(*l2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div

    if x < min(l2[0][0], l2[1][0]) or x > max(l2[0][0], l2[1][0]) or y < min(l2[0][1], l2[1][1]) or y > max(l2[0][1], l2[1][1]):
        return False
    else:
        return x,y

# 0 0 3 3
# 1
# 4 1 2 2 2 2 1 1 1

main_line = list(map(int, input().split()))
num = int(input())

print(line_intersection((A, B), (C, D)))