inp = list(map(int, input().split()))
n = inp[0]
m = inp[1]
place = {}
car = {}
money = 0
stack = []


def get():
    global place
    for id in place:
        if place[id]['owned'] == 0:
            return id
    return 0


def park(auto):
    global car, place, money
    pid = get()
    if pid:
        car[auto]['parked'] = pid
        place[pid]['owned'] = auto
        money += car[auto]['weight'] * place[pid]['price']
    else:
        stack.append(auto)


def unpark(auto):
    global car, place
    place[car[auto]['parked']]['owned'] = 0
    car[auto]['owned'] = 0


for p in range(n):
    place[p + 1] = {}
    place[p + 1]['price'] = int(input())
    place[p + 1]['owned'] = 0
for w in range(m):
    car[w + 1] = {}
    car[w + 1]['weight'] = int(input())
    car[w + 1]['parked'] = 0
for i in range(2 * m):
    auto = int(input())
    if auto > 0:
        park(auto)
    else:
        unpark(-auto)
        if len(stack):
            park(stack[0])
            stack = stack[1:]
print(money)
input()
