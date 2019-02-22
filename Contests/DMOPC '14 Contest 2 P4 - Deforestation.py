import sys
input = sys.stdin.readline
length = int(input())

nums = [0 for a in range(length)];
sums = [0 for a in range(length)];

for a in range(length):
    nums[a] = int(input())
    if a > 0:
        sums[a] = sums[a - 1] + nums[a]
    else:
        sums[a] = nums[a]

for a in range(int(input())):
    val = input().split()
    val[0] = int(val[0])
    val[1] = int(val[1])
    if (val[0] == 0):
        print(sums[val[1]])
    else:
        print(sums[val[1]] - sums[val[0] - 1])