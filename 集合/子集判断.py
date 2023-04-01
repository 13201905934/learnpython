# 子集判断 子集指的是一个集合中的元素全部存在于另一个集合中 存在返回true
friends = {'fox', 'dog', 'pig', 'rabbit', 'tiger', 'cat', 'bear'}
pets = {'dog', 'cat', 'rabbit'}
print(pets.issubset(friends))  # True
