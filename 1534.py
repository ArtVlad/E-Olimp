from math import ceil


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def f(x, arr):
    n = len(arr)
    res = 0
    for i in range(1, 1 << n):
        lcm = 1
        bits = 0
        for j in range(0, n):
            if i & 1 << j:
                bits += 1
                temp = gcd(lcm, arr[j])
                lcm = lcm / temp * arr[j]
                if lcm > x:
                    break
        if bits % 2:
            res += x / lcm
        else:
            res -= x / lcm
    return res


lines = open('input.txt', 'r').read().split('\n')
length = len(lines)

open('output.txt', 'w').write('')
out = open('output.txt', 'a')

for i in range(0, length, 2):
    [left, right] = list(map(int, lines[i].split()))
    dividers = list(map(int, lines[i+1].split()))
    dividers.pop(0)
    result = 0

    if dividers[0] == 1:
        result = right - left + 1
    else:
        result = ceil(f(right, dividers) - f(left - 1, dividers))

    out.write(str(result) + '\n')
    print(result)

out.close()