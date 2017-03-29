num = int(input())
strings = [None] * num

for i in range(num):
    strings[i] = input()


def get(in_string):
    first_key = in_string[0]
    for i, key in enumerate(in_string):
        if key == first_key and i != 0:
            if len(in_string) / i == int(len(in_string) / i) and in_string[0:i] * int(len(in_string) / i) == in_string:
                return i
    return len(in_string)


for string in strings:
    print(get(string))
    print()
