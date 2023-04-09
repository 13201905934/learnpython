class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)


v1 = Vector(2, 10, 3)
v2 = Vector(5, -2, 8)
v = v1 + v2
print('Vector(' + str(v.x) + ',' + str(v.y) + ',' + str(v.z) + ')')
