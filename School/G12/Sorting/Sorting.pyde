# add_library("sound")
ls = [random(0, 500) for _ in range(300)]
_ls = ls[:]
access = []
high = []
checked = []
tick = 0

def setup():
    size(1000, 700)
    thread("insertion_sort")
    print(_ls)

def render():
    background(0)

    textSize(35)
    text("Merge Sort", 10, 50)

    bw = 1150 / len(ls)
    bh = 600 / max(ls)

    for i in range(len(ls)):
        #if ls[i] in splot:
        #    fill(0, 0, 255)
        if i in checked:
            fill(0, 255, 0)
        elif i in access:
            fill(255, 0, 0)
        elif i in high:
            fill(0, 0, 255)
        else:
            fill(255)
        rect(i * bw, 700 - (bh * ls[i]), bw, bh * ls[i])

def draw():
    global tick, ls, splot
    tick += 1
    #if sorted(_ls) == splot:
    #    thread("bruh")
    render()

def bruh():
    global ls, splot

    for i in range(len(splot)):
        ls[i] = splot[i]
        delay(50)
    splot = []
    thread("verify")

def check(val):
    global access
    if val in access:
        access.pop(access.index(val))
    else:
        access.append(val)

def highlight(val):
    global high
    if val in high:
        high.pop(high.index(val))
    else:
        high.append(val)

def verify():
    for i in range(len(ls)):
        checked.append(i)
        delay(10)

def bubble_sort():
    global ls

    for j in range(len(ls) - 1):
        for a in range(len(ls) - j - 1):
            check(a + 1) # ACCESS
            if ls[a] > ls[a + 1]:
                ls[a], ls[a + 1] = ls[a + 1], ls[a]
            # delay(1)
            check(a + 1) # ACCESS
        delay(10)
    verify()

def selection_sort():
    global ls

    for a in range(len(ls) - 1):
        smallest = [a, ls[a]] # i, val
        highlight(smallest[0]) # HIGHLIGHT
        for b in range(a, len(ls)):
            check(b + 1) # ACCESS
            if ls[b] < smallest[1]:
                highlight(smallest[0]) # HIGHLIGHT
                smallest = [b, ls[b]]
                highlight(smallest[0]) # HIGHLIGHT
            delay(1)
            check(b + 1) # ACCESS
        delay(1)
        ls[a], ls[smallest[0]] = ls[smallest[0]], ls[a]
        highlight(smallest[0]) # HIGHLIGHT

    verify()

def insertion_sort():
    global ls

    for i in range(1, len(ls)):
        j = i
        check(i) # ACCESS
        delay(10)
        while (j > 0) and ls[j - 1] > ls[j]:
            highlight(j - 1)
            ls[j], ls[j - 1] = ls[j - 1], ls[j]
            # delay(1)
            highlight(j - 1)
            j = j - 1
        check(i)
    verify()

def merge_sort(lst = None, start = None, stop = None):
    global ls, splot
    splot = []
    if lst == None:
        lst = ls[:]
        start = 0
        stop = len(lst)
    if len(lst) == 1:
        return lst
    else:
        left = lst[:len(lst) // 2]
        right = lst[len(lst) // 2:]
        left = merge_sort(left, start, stop - len(lst) // 2)
        right = merge_sort(right, start + len(lst) // 2 - 1, stop)

    li, ri = 0, 0
    result = []
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            result.append(left[li])
            li += 1
        else:
            result.append(right[ri])
            ri += 1
    result += left[li:]
    result += right[ri:]
    splot = result[:]
    if start != None and stop != None:
        print(result)
        for i in range(len(result)):
            delay(3)
            print("accesssing", i)
            ls[start + i] = result[i]
    return result
