# 创建一个朋友列表 练习列表的添加
friends = ['fox', 'dog', 'pig']
# 创建一个颜色列表
colors = ['white', 'yellow', 'black']
# 将colors添加到friends
friends[len(colors):] = colors
# 打印friends
print(friends)  # ['fox', 'dog', 'pig', 'white', 'yellow', 'black']

# 5.1复习
fruit = ['apple', 'banana', 'll']
zoon = ['dog', 'one']
# 将zoon添加到fruit中
fruit[len(zoon):] = zoon
print(fruit)  # ['apple', 'banana', 'dog', 'one']
