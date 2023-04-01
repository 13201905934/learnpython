# 集合中的元素是无序且没有索引的
colors = {'red', 'yellow', 'blue'}
print(colors)
print(type(colors))

# 集合遍历
for color in colors:
    print(color)

# 查找某个元素是否存在在集合中
if 'red' in colors:
    print("red在集合中")

# 求集合的长度和在集合中添加元素
print(len(colors))
colors.add('this')
print(colors)

# 用Update方法添加
colors.update(['black', 'bear', 'tiger'])
print(colors)  # {'bear', 'red', 'blue', 'tiger', 'this', 'yellow', 'black'}

# pop删除集合元素,删除的元素是随机的
# one = colors.pop()
# print(colors)
# print(one)

# remove discard区别：被删除元素不存在时discard不会报错
# colors.remove('this')
# print(colors)
colors.discard('black')
print(colors)

# del 会将整个集合删掉,clear只会清空集合内容
# setOne={'one','two'}
# del setOne
# print(setOne)

setTwo = {'one', 'two'}
setTwo.clear()
print(setTwo)
setTwo.add('three')
print(setTwo)  # {'three'}

# set构造器创建集合
friends = set(('fox', 'dog', 'monkey', 'pig'))
print(friends)  # {'pig', 'fox', 'dog', 'monkey'}

friendsOne = set(('dog',))
print(friendsOne)  # {'dog'}
friendsTwo = set(('dog'))
print(friendsTwo)  # {'g', 'd', 'o'}
