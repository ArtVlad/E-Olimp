input()
first = {}
for a in input().split():
    first[a] = True
input()
for a in input().split():
    print('YES' if a in first else 'NO')
