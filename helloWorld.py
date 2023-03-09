print("hello world!")
if 5 > 2:
    print("5>2是正确的")

x = "帅气的"


def myfunc():
    print("python is " + x)


myfunc()

# 字符串索引，从后面开始是从负1开始,例如[-5,-2]从负5开始不包含-2的字符串 orl
y = "hello,world!"
print(y[-5:-2])

# 检查以下文本中是否存在短语 "ina"：
txt = "china is a great country"
b = "ina" in txt
print(b)

# 使用 format() 方法将数字插入字符串：
age = 63
txt = "My name is Bill, I am {}"
print(txt.format(age))
# False
print(bool(0))

# 列表创建
thisList = ["apple", "banana", "cherry"]
# 遍历
for n in thisList:
    print(n)
# 插入项目作为第二个位置：
thisList.insert(1, "happy")  # ['apple', 'happy', 'banana', 'cherry']
print(thisList)

# pop() 方法删除指定的索引（如果未指定索引，则删除最后一项）：cherry
print(thisList.pop())

# del 关键字删除指定的索引
del thisList[0]
print(thisList)  # ['happy', 'banana']

# 使用 copy() 方法来复制列表：
copyList = thisList.copy()
print(copyList)  # ['happy', 'banana']

# 制作副本的另一种方法是使用内建的方法 list()
copyListOne = list(thisList)
print(copyListOne)  # ['happy', 'banana']

# 连接两个列表的另一种方法是将 list2 中的所有项一个接一个地追加到 list1 中：
listOne = ["a", "b", "c"]
listTwo = [1, 2, 3]
for c in listTwo:
    listOne.append(c)
print(listOne)  # ['a', 'b', 'c', 1, 2, 3]

# 使用 extend() 方法将 list2 添加到 list1 的末尾：
listOne.extend(listTwo)
print(listOne)  # ['a', 'b', 'c', 1, 2, 3, 1, 2, 3]

# 元组是有序且不可更改的集合,在 Python 中，元组是用圆括号编写的
thisTuple = ("life", "is", "good")
print(thisTuple)
# 元组创建后就不可改变，可以将元组转换为列表，更改列表，然后将列表转换回元组。
changeTuple = list(thisTuple)
changeTuple[2] = "better"
thisTuple = tuple(changeTuple)
print(thisTuple)  # ('life', 'is', 'better')
# 打印元组中的项目数量：
print(len(thisTuple))
# 单项元组，别忘了逗号
tupleOne = ("pick",)
print(tupleOne)

# del 关键字可以完全删除元组：
del tupleOne
# print(tupleOne)#NameError: name 'tupleOne' is not defined

# 集合是无序和无索引的集合。在 Python 中，集合用花括号编写,无法用索引访问，集合一旦创建，您就无法更改项目，但是您可以添加新项目
thisSet = {"first", "sencond", "third"}
print(thisSet)  # {'first', 'third', 'sencond'}
thisSet.add("asas")
print(thisSet)
# 使用 update() 方法将多个项添加到集合中
thisSet.update(["you", "are", "better"])
print(thisSet)
# 要删除集合中的项目，请使用 remove() 或 discard() 方法,如果要删除的项目不存在,remove()会报错
thisSet.discard("you")
print(thisSet)

# 字典是一个无序、可变和有索引的集合。在 Python 中，字典用花括号编写，拥有键和值
thisDict = {
    "name": "qiangwengang",
    "age": 24,
    "sex": "man"
}
print(thisDict)
# 通过键获取值
print(thisDict["name"])
# 通过get获取值
print(thisDict.get("name"))

# 您可以通过引用其键名来更改特定项的值：
thisDict["name"] = "qiangwenjie"
print(thisDict["name"])
# 通过使用 items() 函数遍历键和值：
for x, y in thisDict.items():
    print(x, y)
# 检查字典中是否存在 "name"：
if x in thisDict:
    print("yes,name is exsits")

# 通过使用新的索引键并为其赋值，可以将项目添加到字典中
thisDict["hobby"] = "basketball"
print(thisDict)  # {'name': 'qiangwenjie', 'age': 24, 'sex': 'man', 'hobby': 'basketball'}
# 词典也可以包含许多词典，这被称为嵌套词典
myFamily = {
    "person1": {
        "name": "qiangwengang",
        "age": 24
    },
    "person2": {
        "name": "qiangwenjie",
        "name": 18
    },
    "person3": {
        "name": "qiangjuanxian",
        "age": 51
    }
}
print(myFamily)

x = 90
y = 90
if x < y:
    print("x小于y")
else:
    print("x大于y")
# if 语句不能为空，但是如果您处于某种原因写了无内容的 if 语句，请使用 pass 语句来避免错误

if x > y:
    pass

# 循环
i = 1
while i < 7:
    i += 1
    if i > 3:
        break
print(i)

b = 1
while b < 5:
    b += 1
    if b == 3:
        continue
    print(b)
