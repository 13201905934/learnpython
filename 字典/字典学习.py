# 字典创建
dog = {
    'name': 'black tiger',
    'color': 'black',
    'age': 3
}
print(dog)
print(type(dog))

# 用循环遍历字典和测试某个元素是否存在
for i in dog:
    print(i)
# name
# color
# age

# 值的显示
print(dog['name'])
for i in dog:
    print(dog[i])

# 循环遍历显示键和值items
for k, v in dog.items():
    print(k, v)
for k, v in dog.items():
    print(str(k) + ':' + str(v))
