# 超集判断 超集指的是一个集合中的元素全部存在于另一个集合中 存在返回true
friends = {'fox', 'dog', 'pig', 'rabbit', 'tiger', 'cat', 'bear'}
pets = {'dog', 'cat', 'rabbit'}
print(friends.issuperset(pets))  # True
