d = ('age', 'weight', 'price')
dog = dict.fromkeys(d, 0)
print(dog)
# fromkeys中参数没有0时，默认为none

d1 = ('age', 'weight', 'price')
dog1 = dict.fromkeys(d1)
print(dog1)  # {'age': None, 'weight': None, 'price': None}

# 5.1练习 fromkeys(m, 0)默认赋值
m = ('age', 'sex')
m1 = dict.fromkeys(m, 0)
print(m1)  # {'age': 0, 'sex': 0}

# 5.24号练习
k = ('age', 'sex', 'price')
kk = dict.fromkeys(k, 0)
print(kk)  # {'age': 0, 'sex': 0, 'price': 0}
