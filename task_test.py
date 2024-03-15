class GeomRange:
    def __init__(self, start, step, stop):
        self.start = start
        self.step = step
        self.stop = stop
        self.__value = self.start


g = GeomRange(1, 1.2, 2)

it = iter(g); res = next(g)
print(it)
print(res)