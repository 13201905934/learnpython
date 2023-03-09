def my_function():
    print("学习函数")


my_function()


# 参数使用list,参数可以是任何数据类型（字符串、数字、列表、字典等）
def first_function(foodList):
    for i in foodList:
        print(i)


foodList = ["apple", "cherry", "banana"]
first_function(foodList)


# 返回值
def sencond_function(x):
    return 5 * x


print(sencond_function(5))


# 如果参数数目未知，请在参数名称前添加 *：
def th_myfunction(*person):
    print("my best lover is " + person[1])


th_myfunction("lingMing", "xiaoHong")


# 练习一个递归
def y_myfunction(m):
    if m > 0:
        result = m + y_myfunction(m - 1)
        print(result)
    else:
        result = 0
    return result


y_myfunction(3)

# lambda函数
x = lambda a: a + 5
print(x(5))  # 10
y = lambda a, b, c: a + b + c
print(y(1, 2, 3))


def function(n):
    return lambda a: a + n


z = function(5)
print(z(5))  # 10


# 类的学习
class myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfun(self):
        print("my lover is " + self.name)


p = myclass("liming", "16")
p.myfun()


# 创建myclass子类
class yourclass(myclass):
    pass


p1 = yourclass("xiaobai", 21)
p1.myfun()


# 添加属性，和继承
class aclass(myclass):
    def __init__(self, name, age, sex):
        myclass.__init__(self, name, age)
        self.sex = sex

    def fun(self):
        print("今年" + str(self.age))


p2 = aclass("linHua", 18, "man")
p2.fun()


class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fun(self):
        print("我喜欢的小狗是" + self.name)


dog1 = dog('doudou', "18")
dog1.fun()
