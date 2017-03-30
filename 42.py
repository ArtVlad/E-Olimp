def make_triangle(arr):
    return list(map(lambda pair: list(map(int, pair)), [[arr[0], arr[2], arr[4]], [arr[1], arr[3], arr[5]]]))


def find_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    if y2 == y1 and y4 == y3:
        return False
    elif y2 != y1 and y4 != y3:
        k1 = (x2 - x1) / (y2 - y1)
        k2 = (x4 - x3) / (y4 - y3)
        if k1 == k2:
            return False
    if x2 == x1 and x4 == x3:
        return False

    # TODO x = const
    if x2 == x1 or x4 == x3:
        return False

    x = -((x1 * y2 - x2 * y1) * (x4 - x3) - (x3 * y4 - x4 * y3) * (x2 - x1)) / ((y1 - y2) * (x4 - x3) - (y3 - y4) * (x2 - x1))
    y = ((y3 - y4) * -x - (x3 * y4 - x4 * y3)) / (x4 - x3)
    # print(x1,-x,x2,'--',x3,-x,x4, (x1 <= -x <= x2 or x2 <= -x <= x1) and (x3 <= x <= x4 or x4 <= x <= x3))
    # print(y1, y,y2,'--',y3, y,y4, (y1 <=  y <= y2 or y2 <=  y <= y1) and (y3 <= y <= y4 or y4 <= y <= y3))
    if (x1 <= x <= x2 or x2 <= x <= x1) and (x3 <= x <= x4 or x4 <= x <= x3) and (y1 <= y <= y2 or y2 <= y <= y1) and (
                y3 <= y <= y4 or y4 <= y <= y3):
        return [x, y]
    else:
        return False


def point_in_triangle(point, triangle):
    result = [False, False]
    for coord in range(2):
        for num in range(3):
            if triangle[0][num] < point[0] < triangle[0][(num+1)%3] or triangle[0][(num+1)%3] < point[0] < triangle[0][num]:
                result[coord] = True
                break
    return result


first = make_triangle('2 2 2 6 8 4'.split() or input().split())
second = make_triangle('5 4 11 6 11 2'.split() or input().split())

print(first)
print(second)

for i in range(3):
    for j in range(3):
        point = find_intersection(first[0][i], first[1][i], first[0][(i + 1) % 3], first[1][(i + 1) % 3], second[0][j], second[1][j], second[0][(j + 1) % 3], second[1][(j + 1) % 3])
        if point:
            print(point)
print('\nFirst in Second')
for i in range(3):
    print([first[0][i], first[1][i]], point_in_triangle([first[0][i], first[1][i]],second))
print('\nSecond in First')
for i in range(3):
    print([second[0][i], second[1][i]], point_in_triangle([second[0][i], second[1][i]],first))