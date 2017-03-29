from math import fabs as abs


def compare(in_str):
    str1 = in_str[0]
    str2 = in_str[1]
    de = 0
    obj = {}
    for a in str1:
        if a not in obj:
            obj[a] = 0
        obj[a] += 1
    for a in str2:
        if a not in obj:
            obj[a] = 0
        obj[a] -= 1
    for a in obj:
        if obj[a] != 0:
            de += int(abs(obj[a]))
    return de


num = int(input())
pairs = []

for x in range(num):
    pairs.append([])
    pairs[x].append(str(input()))
    pairs[x].append(str(input()))

for x, pair in enumerate(pairs):
    print('Case #' + str(x + 1) + ':  ' + str(compare(pair)))
