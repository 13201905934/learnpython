import random

i = 1
x = random.randint(0, 98)
y = int(input('请输入0-98的一个数字\n然后查看是否与计算机产生的随机数一样：'))
while x != y:
    if x > y:
        print("第" + str(i) + '次输入的数小于随机数')
        y = int(input("请再次输入数字："))
    else:
        print("第" + str(i) + '次输入的数字大于计算机产生的数')
        y = int(input("请再次输入数字："))
    i = i + 1
else:
    print("恭喜，第" + str(i) + "次输入的数字与计算机产生的随机数" + str(y) + '一样')
