# 定义一只狗
class dog:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age


# 定义一只猫
class cat:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


# 初始化狗
dog1 = dog('linna', 98, 10)
dog2 = dog('liming', 15, 3)

# 初始化狗
cat1 = cat('huh', 15, 'man')
print(dog1.name)
print(dog2.weight)
print(cat1.sex)
