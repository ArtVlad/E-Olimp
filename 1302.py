from math import sqrt

array = [2]
count = int(input())
inputs = [None] * count
outputs = [None] * count
isSimple = {}


def goIn(number, x):
    if not number == int(number) or number < 1:
        return False
    elif number == 1:
        return True
    else:
        return goIn(number / x, x)


def getSimple(f, t):
    mbarr = 0
    for i in range(f, t):
        for j in array:
            if j < i and goIn(i, j):
                mbarr += 1
    return mbarr


n = 5
for i in range(count):
    inputs[i] = list(map(int, input().split()))
    n = inputs[i][1] if inputs[i][1] > n else n

for i in range(3, n + 1, 2):
    if (i > 10) and (i % 10 == 5):
        continue
    for j in array:
        if j * j - 1 > i:
            array.append(i)
            break
        if i % j == 0:
            break
    else:
        array.append(i)
for i in range(n):
    for j in array:
        if j < i and goIn(i, j):
            isSimple[i] = True

for i in range(count):
    print(getSimple(inputs[i][0], inputs[i][1]))