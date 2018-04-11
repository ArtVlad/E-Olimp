lines = open('input.txt', 'r').read().split('\n')
length = len(lines)

for i in range(length):
    lines[i] = list(map(int, lines[i].split()))


def ccw(x1, y1, x2, y2, x3, y3):
    return (y3-y1) * (x2-x1) > (y2-y1) * (x3-x1)


def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    return ccw(x1, y1, x3, y3, x4, y4) != ccw(x2, y2, x3, y3, x4, y4) and ccw(x1, y1, x2, y2, x3, y3) != ccw(x1, y1, x2, y2, x4, y4)


def check_intersection():
    for i in range(length):
        for j in range(i, length):
            if i != j and intersect(*lines[i], *lines[j]):
#            if i != j and intersect(lines[i][0], lines[i][1], lines[i][2], lines[i][3], lines[j][0], lines[j][1], lines[j][2], lines[j][3]):
                return True
    return False


open('output.txt', 'w').write('intersect' if check_intersection() else 'NOT intersect')
