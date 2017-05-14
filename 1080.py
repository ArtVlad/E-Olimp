

def compare(str1,str2):
    de = 0
    obj = {}
    for a in str1:
        if a not in obj:
            obj[a] = 0
        obj[a] += 1
    for a in str2:
        if a not in obj:
            obj[a] = 0
        obj[a] -= 1
    for a in obj:
        if obj[a] != 0:
            de += obj[a] if obj[a] > 0 else -obj[a]
    return de

	
for x in range(int(input())):
    print('Case #' + str(x + 1) + ':  ' + str(compare(input(), input())))

