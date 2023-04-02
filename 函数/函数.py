def findings(f):
    print(f)


findings("奋斗的过程都是自我坚持的过程")
findings("投资都期望回报")


# 函数参数的默认值
def pet(p='rabbit'):
    print('i love my ' + p + ' very much! ')


pet()
pet('cat')


# 以一个列表作为函数的参数
def friend(f):
    for i in f:
        print(i)


pets = ['monkey', 'pig', 'car']
friend(pets)

m = findings("返回值为空")  # None
print(m)
print(type(m))
