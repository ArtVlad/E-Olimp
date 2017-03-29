s = ''


def find(normal, centered, size):
    global s
    # print(normal, centered, size)
    if size == 0:
        return
    if size == 1:
        s += normal[0]
        return

    find_root = 0

    while centered[find_root] != normal[0] and find_root < len(centered):
        find_root += 1

    find(normal[1:], centered, find_root)
    find(normal[find_root + 1:], centered[find_root + 1:], size - 1 - find_root)
    s += normal[0]


def go(normal, centered, size):
    global s
    s = ''
    find(normal, centered, size)
    return s


test = int(input())
arr = [None] * test
for i in range(test):
    inp = input().split()
    arr[i] = go(inp[1], inp[2], int(inp[0]))
print('\n'.join(arr))
