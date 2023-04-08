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

    # 创建bark()方法
    def bark(self):
        print('miao miao i am: ' + self.name)

    # 创建睡觉方法
    def sleep(self):
        print('我做了一个美梦，梦见我正在和心爱的人散步，湖水轻轻荡漾！')

    # 创建喝水方法
    def drink(self):
        print(self.name + '有点渴了，正在喝水')


# 初始化狗
dog1 = dog('linna', 98, 10)
dog2 = dog('liming', 15, 3)

# 初始化狗
cat1 = cat('huh', 15, 'man')
print(dog1.name)
print(dog2.weight)
print(cat1.sex)
# 调用猫的方法
cat1.bark()
cat1.sleep()
cat1.drink()
print(type(dog2))  # <class '__main__.dog'>
print(dog2)
# 修改对象属性，这里以猫作为示例
cat1.name = 'lina'
cat1.age = 15
cat1.sex = 'F'
cat1.bark()
cat1.sleep()
cat1.drink()
# 删除对象用del 例如 del dog1
