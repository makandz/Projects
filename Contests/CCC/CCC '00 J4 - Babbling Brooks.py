def join_strms(s):
    s -= 1
    st = paths
    newst = st[s] + st[s+1]
    st.remove(st[s+1])
    st.remove(st[s])
    st.insert(s, newst)
    return st

def split_strms(s, l):
    s -= 1
    st = paths
    perc = l/100
    # print(perc)
    left = st[s]*perc
    right = st[s] - left
    st.remove(st[s])
    st.insert(s, round(right))
    st.insert(s, round(left))
    return st

n = int(input())
paths = []
for i in range(n):
    val = int(input())
    paths.append(val)

data = int(input())

while data != 77:
    if data == 99:
        stream = int(input())
        left = int(input())
        paths = split_strms(stream, left)
    elif data == 88:
        stream = int(input())
        paths = join_strms(stream)
    data = int(input())

for i in paths:
    print(i, end=' ')