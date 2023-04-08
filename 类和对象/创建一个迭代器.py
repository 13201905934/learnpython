class TenNUmbers:
    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        n = self.x
        self.x += 10
        return n


num = TenNUmbers()
numIter = iter(num)
print(next(numIter))
print(next(numIter))
