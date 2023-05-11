friends = ['cat', 'dog', 'monkey', 'pig', 'cat', 'dog']
# 去除重复元素
friends = list(dict.fromkeys(friends))
print(friends)


# 定义一个去除重复项的函数
def remove_dup(s):
    return list(dict.fromkeys(s))


print(remove_dup(['cat', 'dog', 'monkey', 'pig', 'cat', 'dog']))
print(remove_dup([3, 3, 5, 6, 6, 7, 7]))

# 5.1去除重复元素练习
cat = ['cat1', 'cat2', 'cat3', 'cat1']
cats = list(dict.fromkeys(cat))
print(cats)  # ['cat1', 'cat2', 'cat3']
