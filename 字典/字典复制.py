dog = {
    'name': 'brown lion',
    'color': 'yellow',
    'age': 13
}

copyDog = dog.copy()
print(copyDog)

copyDog.update({'bread': 'chow chow'})
print(dog)
print(copyDog)

# 5.1复习 字典中添加键值
home = {
    'name': 'ma fang zhen',
    'provice': 'shan xi'
}
home.update({'exists': 'yes'})
print(home)
