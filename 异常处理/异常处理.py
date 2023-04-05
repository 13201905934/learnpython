try:
    print(x)
except:
    print('this program has captured an exception!')

# python提供了标准异常 常见的标准异常 NameError KeyError IndexError TypeError ZeroDivisionError

try:
    print(y)
except NameError:
    print("请先定义该变量")
except:
    print("崩溃了我")

# else 执行是在没有任何错误时
try:
    print("wo shi ge da s b")
except:
    print("检查到异常")
else:
    print('这个程序没有异常')

# finally 不管程序有没有异常他都会执行
try:
    print(y)
except NameError:
    print("请先定义该变量")
except:
    print("崩溃了我")
finally:
    print('finally已经执行')
