from math import fabs, sqrt

EPS = 0.1
y = []
z = []
count_of_triangles = 0


def add_triangle_to_set(x1, y1, z1):
    global count_of_triangles
    y_to_x = y1 / x1
    z_to_x = z1 / x1
    for i in range(count_of_triangles):
        print(y1, y[i])
        if fabs(y1 - y[i]) < EPS and fabs(z1 - z[i]) < EPS:
            return False
    y.append(y1)
    z.append(z1)
    count_of_triangles += 1
    return True


def check_triangle(sides):
    sides.sort()
    if not add_triangle_to_set(sides[0], sides[1], sides[2]):
        return
    m = sqrt(2 * sides[0] * sides[0] + 2 * sides[1] * sides[1] - sides[2] * sides[2]) / 2
    check_triangle([sides[0], m, sides[2] / 2])
    check_triangle([sides[1], m, sides[2] / 2])


for i in range(int(input())):
    triangle = list(map(int, input().split()))
    check_triangle(triangle)
    print(len(y), len(z))

