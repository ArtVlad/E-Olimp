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


for p in range(1, n + 1):
    place[p] = {}
    place[p]['price'] = int(input())
    place[p]['owned'] = 0
for w in range(1, m + 1):
    car[w] = {}
    car[w]['weight'] = int(input())
    car[w]['parked'] = 0
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
