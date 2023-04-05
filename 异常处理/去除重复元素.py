friends = ['cat', 'dog', 'monkey', 'pig', 'cat', 'dog']
# 去除重复元素
friends = list(dict.fromkeys(friends))
print(friends)


# 定义一个去除重复项的函数
def remove_dup(s):
    return list(dict.fromkeys(s))


print(remove_dup(['cat', 'dog', 'monkey', 'pig', 'cat', 'dog']))
print(remove_dup([3, 3, 5, 6, 6, 7, 7]))
