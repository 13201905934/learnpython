print("一班学生人数")
classNum1 = int(input())
# 初始化一个集合
className1 = set()
for item in range(0, classNum1):
    name1 = input("请输入学生%d的名字:" % (item + 1))
    # 加入到集合中去
    className1.add(name1)

print("二班学生人数")
classNum2 = int(input())
# 初始化一个集合
className2 = set()
for item in range(0, classNum2):
    name2 = input("请输入学生%d的名字:" % (item + 1))
    # 加入到集合中去
    className2.add(name2)
# 相同名字,sameName存储着相同名字的集合
sameName = className2.intersection(className1)

print("重名的人是：")
# 打印
for name in sameName:
    print(name)
