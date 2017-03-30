class Array:
    value = {}
    last_plus = True
    last_query = -1

    def __getitem__(self, item):
        return list(self.value.keys())[item]

    def __iter__(self):
        return iter(self.value.keys())

    def __str__(self):
        return ' '.join(map(str, self.value.keys()))

    def add(self, i):
        if self.last_plus:
            num = i
        else:
            num = (i + self.last_query) % 1e9
        self.value[num] = True
        self.last_plus = True
        return self

    def next(self, i):
        self.last_query = -1
        if i in self.value:
            self.last_query = i
        else:
            for e in self:
                if i <= e and (self.last_query == -1 or e < self.last_query):
                    self.last_query = e
        self.last_plus = False
        print(self.last_query)
        return self.last_query

S = Array()
method = {
    '+': S.add,
    '?': S.next
}
for a in range(int(input())):
    inp = input().split()
    method[inp[0]](int(inp[1]))
