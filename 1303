import math
p = [None] * 500001


def merge(buf, l, r):
    if r == l:
        return 0
    m = math.floor((r + l) / 2)
    k = merge(buf, l, m) + merge(buf, m + 1, r)
    xl = l
    xr = m + 1
    cur = 0
    while r - l + 1 != cur:
        if xl > m:
            buf[cur] = p[xr]
            xr += 1
        elif xr > r:
            buf[cur] = p[xl]
            xl += 1
        elif p[xl] > p[xr]:
            buf[cur] = p[xr]
            xr += 1
            k += m - xl + 1
        else:
            buf[cur] = p[xl]
            xl += 1
        cur += 1

    for i in range(cur):
        p[i + l] = buf[i]
    return k

while True:
    n = int(input())
    b = [None] * n
    if n == 0:
        break
    for i in range(n):
        p[i] = int(input())
    print(merge(b, 0, n - 1))
