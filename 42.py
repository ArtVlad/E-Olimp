def make_triangle(arr):
    return list(map(lambda pair: list(map(int, pair)), [[arr[0], arr[2], arr[4]], [arr[1], arr[3], arr[5]]]))


def find_point(x1, y1, x2, y2, x3, y3, x4, y4):
    if y2 == y1 and y4 == y3:
        return False
    elif y2 != y1 and y4 != y3:
        k1 = (x2 - x1) / (y2 - y1)
        k2 = (x4 - x3) / (y4 - y3)
        if k1 == k2:
            return False

    if x2 == x1 and x4 == x3:
        return False
    if x1 == x2 or x3 == x4:
        return False
    x = ((x1 * y2 - x2 * y1) * (x4 - x3) - (x3 * y4 - x4 * y3) * (x2 - x1)) / (
    (y1 - y2) * (x4 - x3) - (y3 - y4) * (x2 - x1))
    y = ((y3 - y4) * x - (x3 * y4 - x4 * y3)) / (x4 - x3)
    return [-x, y]


first = make_triangle('2 2 2 6 8 4'.split() or input().split())
second = make_triangle('5 4 11 6 11 2'.split() or input().split())

print(first)
print(second)

for i in range(3):
    for j in range(3):
        point = find_point(first[0][i], first[1][i], first[0][(i+1)%3],first[1][(i+1)%3],second[0][j], second[1][j], second[0][(j+1)%3],second[1][(j+1)%3])
        if point:
            print(point)
