# the best friend is your dog!
print('the best {} is your {}!'.format('friend', 'dog'))
# the best pet is your cat!
print('the best {} is your {}!'.format('pet', 'cat'))
# 胡鹏、狗友和猪队友
print('{0}、{1}和{2}'.format('胡鹏', '狗友', '猪队友'))
# 狗友、胡鹏和猪队友
print('{1}、{0}和{2}'.format('胡鹏', '狗友', '猪队友'))
# I love this world and I love you
print('I {v} this world and {u} love you'.format(v='love', u='I'))

employee = {'武大郎': 7474, '潘金莲': 6868, '西门庆': 9898, '童铁蛋': 8888}
# format(**employee) **用法
print('武大郎：{武大郎:d};潘金莲：{潘金莲:d};西门庆：{西门庆:d};童铁蛋：{童铁蛋:d}'.format(
    **employee))  # 武大郎：7474;潘金莲：6868;西门庆：9898;童铁蛋：8888

# 可以在format()方法中使用变量和由变量所组成的表达式
for i in range(1, 11):
    # i ** 2=i*i i ** 3=i*i*i
    print('{0:2d} {1:3d} {2:4d}'.format(i, i ** 2, i ** 3))
