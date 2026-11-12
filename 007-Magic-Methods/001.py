class Fibs:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break

assert f == 1597
