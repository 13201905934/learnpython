# 创建一个朋友列表 练习列表的添加
friends = ['fox', 'dog', 'pig']
# 创建一个颜色列表
colors = ['white', 'yellow', 'black']
# 将colors添加到friends
friends[len(colors):] = colors
# 打印friends
print(friends)   #['fox', 'dog', 'pig', 'white', 'yellow', 'black']
