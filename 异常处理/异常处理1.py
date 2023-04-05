def divide(x, y):
    try:
        r = x / y
    except ZeroDivisionError:
        print('division is zero')
    else:
        print('结果：', r)
    finally:
        print('finally执行了')


divide(8, 4)
divide(6, 0)
divide('8', '4')  # finally执行了
