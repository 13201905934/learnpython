class pet:
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


# 创建一个pet的子类,只需要将父类当作参数传给子类
class rabbit(pet):
    # 在子类中添加自己的__init__
    def __init__(self, name, age, sex, weight):
        pet.__init__(self, name, age, sex)
        self.weight = weight

    # 在子类中创建自己的方法
    def move(self):
        print('我正在移动' + str(self.weight) + '重的身体')

    # 方法的重载
    def drink(self):
        print('被打扰我！我真的真的很渴！')
        # 还想调用父类的重载方法 super(子类名，对象名).方法
        # super(rabbit, rabitt2).drink()


rabbit1 = rabbit('xiaobai', 20, 'F', 20)
print(rabbit1.name)
rabbit1.sleep()
rabbit1.drink()
rabbit1.bark()
# 创建另一只兔子
rabitt2 = rabbit('yuanrun', 20, 'M', 100)
print(rabitt2.weight)
rabitt2.bark()  # miao miao i am: yuanrun
rabitt2.move()  # 我正在移动100重的身体
rabitt2.drink()  # 被打扰我！我真的真的很渴！  由此可见方法已经重载

# 还想调用父类的重载方法 super(子类名，对象名).方法
super(rabbit, rabitt2).drink()  # yuanrun有点渴了，正在喝水
