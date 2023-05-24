things = 'you know i am very busy'


def thing():
    global things
    print('things: ' + things)


thing()

# 5.24 全局变量练习
count = 'yes,maybe it is a count'


def lunch():
    print('this is a' + count)


lunch()
