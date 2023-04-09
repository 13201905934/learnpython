class TenNumber:
    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        if self.x <= 150:
            n = self.x
            self.x += 10
            return n
        else:
            raise StopIteration


num = TenNumber()
# numIter = iter(num)
for i in iter(num):
    print(i)
