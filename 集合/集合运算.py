# 集合并交差集合运算
friends = {'fox', 'dog', 'pig'}
pets = {'dog', 'cat', 'rabbit'}
f = friends.union(pets)
print(f)  # {'rabbit', 'dog', 'cat', 'pig', 'fox'}

friends1 = {'fox', 'dog', 'pig', 'cat'}
pets1 = {'dog', 'cat', 'rabbit'}
cats = {'tiger', 'lion', 'cat'}
f1 = friends1.union(pets1, cats)
print(f1)  # {'rabbit', 'pig', 'lion', 'tiger', 'cat', 'dog', 'fox'}

# 交集
print(friends.intersection(pets))  # {'dog'}
print(friends1.intersection(pets1, cats))  # {'cat'}

# friends.intersection_update()练习 执行后friends内容只有公共部分dog
friends.intersection_update(pets)
print(friends)  # {'dog'}

friends1.intersection_update(pets1, cats)
print(friends1)  # {'cat'}

# 差集
o1 = {'cat', 'dog', 'pig'}
o2 = {'dog', 'cat', 'rabbit'}
f2 = o1.difference(o2)
print(f2)  # {'pig'}

# difference_update a在b中不存在的元素赋值给a
friends2 = {'cat', 'dog', 'pig', 'fox'}
pets3 = {'dog', 'cat', 'rabbit'}
friends2.difference_update(pets3)
print(friends2)  # {'fox', 'pig'}

# 平衡差集使用 symmetric_difference 只在一个集合中出现的元素
friends3 = {'fox', 'dog', 'pig'}
pets4 = {'dog', 'cat', 'rabbit'}
fp = friends3.symmetric_difference(pets4)
print(fp)  # {'fox', 'cat', 'rabbit', 'pig'}

# 只在一个集合中出现的元素赋值给friends3
friends3.symmetric_difference_update(pets4)
print(friends3)  # {'pig', 'fox', 'cat', 'rabbit'}
