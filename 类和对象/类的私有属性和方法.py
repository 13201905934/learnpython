class Order:
    # 在属性名前面加两个下划线就是私有属性
    __innerOrder = 0  # 私有属性
    publicOrder = 2250  # 共有属性 无论私有公有类里边都可以访问

    def orderNum(self):
        self.__innerOrder += 1
        self.publicOrder += 1
        print(self.__innerOrder)

    # 定义一个私有方法 在方法名前面加两个下划线就是私有方法
    def __move(self):
        print('move move 快速移动！')

    # 在copyMove里调用私有方法__move，外部不可调用
    def copyMove(self):
        self.__move()


order1 = Order()
order1.orderNum()
print(order1.publicOrder)
print(order1.publicOrder)
# print(order1.__innerOrder) 会报没有权限的错误
order1.copyMove()
# order1.__move()  外部调用就报错了，没有权限
