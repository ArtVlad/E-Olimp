
def get_max(arr, f, t):
    max_sum = None
    for i in range(f, t):
        for j in range(i, t):
            current_sum = sum(arr[i:j+1])
            # print('>', i+1, j+1, arr[i:j+1], current_sum)
            if max_sum is None or max_sum < current_sum:
                max_sum = current_sum
    return max_sum


n = int(input())
a = list(map(int, input().split()))

for line in range(int(input())):
    [cmd, x, y] = list(map(int, input().split()))
    if cmd == 0:
        a[x-1] = y
    elif cmd == 1:
        print(get_max(a, x - 1, y))
    else:
        pass


