dog = {
    'name': 'linfeng',
    'color': 'yellow',
    'age': 12
}

dog.pop('color')
print(dog)

# popitem 删除字典最后一项
dog.popitem()
print(dog)

dog1 = {
    'name': 'linfeng',
    'color': 'yellow',
    'age': 12
}

# 用del删除指定的项
del dog1['age']
print(dog1)
