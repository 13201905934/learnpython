d = ('age', 'weight', 'price')
dog = dict.fromkeys(d, 0)
print(dog)
# fromkeys中参数没有0时，默认为none

d1 = ('age', 'weight', 'price')
dog1 = dict.fromkeys(d1)
print(dog1)  # {'age': None, 'weight': None, 'price': None}
