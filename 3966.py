input()  # 1
first = {}  # 1
for a in input().split():  # 1 + N + N
    first[a] = True  # N
input()  # 1
for a in input().split():  # 1 + M + M
    print('YES' if a in first else 'NO')  # ( 1 + 1 ) * M
