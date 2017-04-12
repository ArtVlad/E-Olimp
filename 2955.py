class Array:
    values = []

    def __init__(self, x):
        self.values.append(x)

    def method(self, m, version, element, value='0'):
        version = int(version) - 1
        element = int(element) - 1
        if m == 'create':
            self.create(version, element, int(value))
        else:
            self.get(version, element)

    def create(self, version, element, value):
        self.values.append(list(self.values[int(version)]))
        self.values[-1][element] = value

    def get(self, version, element):
        print(self.values[version][element])

input()
x = Array(input().split())
for i in range(int(input())):
    x.method(*input().split())
