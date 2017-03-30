#def point_in_triangle(point, triangle):
#    result = [False, False]
#    for coord in range(2):
#        for num in range(3):
#            if triangle[0][num] < point[0] < triangle[0][(num + 1) % 3] or triangle[0][(num + 1) % 3] < point[0] < \
#                    triangle[0][num]:
#                result[coord] = True
#                break
#    return result
#
#
#points = [[0, 0], [3, 1], [2, 0]]
#triangle = [[1, 2, 4], [1, -1, 0]]
#for point in points:
#    print(point, point_in_triangle(point, triangle))


def inPolygon(point, triangle):
    c = False
    for i in range(len(triangle[0])):
        if ((triangle[1][i] <= point[1] < triangle[1][i - 1]) or (triangle[1][i - 1] <= point[1] < triangle[1][i])) and (
                    point[0] > (triangle[0][i - 1] - triangle[0][i]) * (point[1] - triangle[1][i]) / (triangle[1][i - 1] - triangle[1][i]) + triangle[0][i]):
            c = True
    return c


print(inPolygon([2, 1], [[1, 2, 4], [1, -1, 0]]))

#
# trx = [tr1, tr2]
# for tr in range(2):
#     trx[tr] == tr1
#     trx[tr-1] == tr2
