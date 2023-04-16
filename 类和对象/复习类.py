# 创建一个Lover类
class lover:
    # 创建一个私有属性
    __order = '这是在回顾类的要点'
    # 公共属性
    test = '测试公共属性'

    def __init__(self, name, age, sex, school):
        self.age = age
        self.name = name
        self.sex = sex
        self.school = school

    def introduce(self):
        print('my lover ' + self.name + '今年' + str(self.age) + ',在' + self.school + '上学')

    def bestThing(self):
        print('我最喜欢和' + self.name + '去公园散步')


# 创建一个wife类，继承lover
class wife(lover):
    def __init__(self, name, age, sex, school, home):
        # 调用父类初始化部分属性
        lover.__init__(self, name, age, sex, school)
        self.home = home

    def introduce(self):
        print('金天晚上想和' + self.name + '在' + self.home + '吃橘子')


# 初始化对象
lover1 = lover('huahua', 26, 'woman', '四川示范大学')
lover1.introduce()
# 初始化wife
wife1 = wife('xiaoli', 26, 'woman', '四川示范大学', 'shanxi')
print(wife1.name)
print(wife1.home)
# 调用父类introduce方法
super(wife, wife1).introduce()
wife1.introduce()
print(lover.test)  # 测试公共属性
# print(lover.__order) 会报错
