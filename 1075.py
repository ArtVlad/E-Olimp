import re

str1 = str(input())
str2 = str(input())


def parse(string):
    obj = {}
    arr = [a for a in re.findall('-?[0-9]*x?\^?[0-9]*', string) if a != '']
    for a in arr:
        x = re.match('(-)?([0-9]+)?(x)?(?:\^([0-9]+))?', a)
        minu = x.group(1)
        coef = x.group(2)
        justx = x.group(3)
        power = x.group(4)

        if coef is None:
            coef = 1

        if justx is None and power is None:
            power = 0
        elif power is None:
            power = 1
        elif justx is None:
            raise NameError('Power for number')

        if minu:
            coef = -int(coef)

        if not power in obj:
            obj[int(power)] = 0
        obj[int(power)] += int(coef)
    return obj


def pri(obj):
    string = ''
    for a in reversed(list(obj.keys())):
        if obj[a] == 0:
            continue
        string += ('+' if obj[a] > 0 and string != '' else '') + (str(obj[a]) if (obj[a] != 1 or a == 0) else '')
        string += ('' if a == 0 else 'x' if a == 1 else 'x^' + str(a))
    return '0' if string == '' else string


obj1 = parse(str1)
obj2 = parse(str2)
obj = {}

for pow1 in obj1:
    for pow2 in obj2:
        pow = pow1 + pow2
        if not pow in obj:
            obj[pow] = 0
        obj[pow] += obj1[pow1] * obj2[pow2]
print(pri(obj))
