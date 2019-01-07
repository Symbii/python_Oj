def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

#Fab是一个迭代类
class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            ret = self.b
            self.n += 1
            self.a, self.b = self.b, self.a + self.b
            return ret
        raise StopIteration

if __name__ == "__main__":
    for x in fab(5):
        print(x)
    print(type(fab(5)))
    s = iter(Fab(5))
    for x in s:
        print(x)