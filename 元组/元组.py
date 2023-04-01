# 不用括号创建元组时，后面的逗号不要省略
pets = 'dog',
print(type(pets))  # <class 'tuple'>
# 元组访问的时候可使用下标

dogs = ('xiaohong', 'baby', 'girls')
print(dogs[1])

# 循环遍历dogs
for dog in dogs:
    if 'baby' == dog:
        print("yeah,i am baby")
    print(dog)

# 元组count方法使用
goods = ('banana', 'monkey', 'dog', 'dog')
print(goods.count('dog'))  # 2
# 元组索引使用
print(goods.index('monkey'))  # 1

# 用del 删除元组
# goods1 = ('beer', 'latiao', 'yanrou')
# del goods1
# print(goods1)  # 会报错，因为goods元组已经删除

# 用tuple构造器创建元组
friends = tuple(('fox', 'dog', 'pig'))
print(friends)
print(type(friends))

# max min sum 使用
digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(max(digits))
print(min(digits))
print(sum(digits))
# 求平均值
print(sum(digits) / len(digits))

# 可以使用乘法将数字元组中每一个元素都初始化为一个特定的值,和列表一样;(2 ** 3,)这里的,号不能省略
digitsOne = 5 * (2 ** 3,)
print(digitsOne)  # (8, 8, 8, 8, 8)
# 利用上述方法初始化字符串元组
friendsOne = 5 * ('girl',)
print(friendsOne)  # ('girl', 'girl', 'girl', 'girl', 'girl')
