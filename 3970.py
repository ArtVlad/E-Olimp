input()
colors = {}
for a in input().split():
    if a not in colors:
        colors[a] = 0
    colors[a] += 1
input()
for a in input().split():
    print(colors[a] if a in colors else 0)
