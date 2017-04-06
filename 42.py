def make_triangle(arr) -> list:
    return list(map(lambda pair: list(map(int, pair)), [[arr[0], arr[2], arr[4]], [arr[1], arr[3], arr[5]]]))


def filt(pointers):
    return [x for i, x in enumerate(pointers) if pointers.index(x) == i]


def length(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5


def find_angle(x1, y1, x2, y2, x3, y3, x4, y4):
    xx1 = x2-x1
    yy1 = y2-y1
    xx2 = x4-x3
    yy2 = y4-y3
    cos = (xx1*xx2+yy1*yy2) / ( (xx1**2 + yy1**2)**0.5 * (xx2**2 + yy2**2)**0.5 )
    sin = (1 - cos**2)**0.5
    return sin


def find_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    def find(x1, y1, x2, y2, x3, y3, x4, y4):
        x = -((x1 * y2 - x2 * y1) * (x4 - x3) - (x3 * y4 - x4 * y3) * (x2 - x1)) / (
            (y1 - y2) * (x4 - x3) - (y3 - y4) * (x2 - x1))
        y = ((y3 - y4) * -x - (x3 * y4 - x4 * y3)) / (x4 - x3)
        if (x1 <= x <= x2 or x2 <= x <= x1) and (x3 <= x <= x4 or x4 <= x <= x3) and (y1 <= y <= y2 or y2 <= y <= y1) and (
                            y3 <= y <= y4 or y4 <= y <= y3):
            return [x, y]
        else:
            return False


    def findv(xx1, yy1, xx2, yy2, xx):
        y = - ((xx1 * yy2 - xx2 * yy1) + (yy1 - yy2) * xx) / (xx2 - xx1)
        if xx1 <= xx <= xx2 or xx2 <= xx <= xx1:
            return [xx, y]
        else:
            return False

    if y2 == y1 and y4 == y3:
        return False
    elif y2 != y1 and y4 != y3:
        k1 = (x2 - x1) / (y2 - y1)
        k2 = (x4 - x3) / (y4 - y3)
        if k1 == k2:
            return False

    if x2 == x1 and x4 == x3:
        return False
    elif x1 == x2:
        return findv(x3, y3, x4, y4, x1)
    elif x3 == x4:
        return findv(x1, y1, x2, y2, x3)
    else:
        return find(x1, y1, x2, y2, x3, y3, x4, y4)


def point_in_triangle(point, triangle) -> bool:
    result = 0
    for i in range(len(triangle[0])):
        if ((triangle[1][i] <= point[1] < triangle[1][i - 1]) or (
                        triangle[1][i - 1] <= point[1] < triangle[1][i])) and (
                    point[0] > (triangle[0][i - 1] - triangle[0][i]) * (point[1] - triangle[1][i]) / (
                            triangle[1][i - 1] - triangle[1][i]) + triangle[0][i]):
            result = 1 - result
    return [False, True][result]


points = []
first = make_triangle( input().split() or ' 1 -2  1 2 -1 0'.split() or '2 2  2 6  8 4'.split() or '0 2 1 1 2 4'.split())
second = make_triangle(input().split() or '-1 -2 -1 2  1 0'.split() or '5 4 11 6 11 2'.split() or '2 1 3 3 1 4'.split())

for i in range(3):
    for j in range(3):
        point = find_intersection(first[0][i], first[1][i], first[0][i - 1], first[1][i - 1], second[0][j],
                                  second[1][j], second[0][j - 1], second[1][j - 1])
        if point:
            points.append(point)
triangles = [first, second]
for tri in range(2):
    for i in range(3):
        if point_in_triangle([triangles[tri][0][i], triangles[tri][1][i]], triangles[tri - 1]):
            points.append([triangles[tri][0][i], triangles[tri][1][i]])
S = 0
points = filt(points)
if len(points) == 3:
    S = 0.5 * ((points[0][0] - points[2][0]) * (points[1][1] - points[2][1]) - (points[1][0] - points[2][0]) * (points[0][1] - points[2][1]))
elif len(points) == 4:
    if find_intersection(*points[0], *points[1], *points[2], *points[3]):
        points[1], points[2] = points[2], points[1]
    elif find_intersection(*points[0], *points[3], *points[1], *points[2]):
        points[1], points[0] = points[0], points[1]
    S = 0.5 * length(*points[0], *points[2]) * length(*points[1], *points[3]) * find_angle(*points[0], *points[2], *points[1], *points[3])
# TODO 5-6 points
print(len(points), round(S if S > 0 else -S, 2))