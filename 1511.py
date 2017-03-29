def max(number1, number2):
    return number1 if number1 > number2 else number2

def min(number1, number2):
    return number1 if number1 < number2 else number2

def cut(length, width, pieces, l):
    print(' ' * l, (length, width, pieces))
    i = 0
    ratio_sides = 0
    result = 0
    if pieces == 1:
        return max(length, width) / min(length, width)
    if pieces == 2 or pieces == 4 or pieces == 8:
        if length >= width:
            return cut(length / 2, width, pieces / 2, l + 1)
        else:
            return cut(length, width / 2, pieces / 2, l + 1)
    for i in range(1, int(pieces)):
        ratio_sides = max(cut(i * length / pieces, width, i, l + 1),
                          cut((pieces - i) * length / pieces, width, pieces - i, l + 1))
        result = min(ratio_sides, result) if result else ratio_sides
        ratio_sides = max(cut(length, i * width / pieces, i, l + 1),
                          cut(length, (pieces - i) * width / pieces, pieces - i, l + 1))
        result = min(ratio_sides, result)
    return result

for i in range(3):
    inp = input().split()
    print(round(cut(float(inp[0]), float(inp[1]), float(inp[2]), 0), 4))
