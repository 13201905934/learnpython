import math

# 显示PI保留到小数点后四位
print(f'the value of PI is approximately {math.pi:.4f}.')  # the value of PI is approximately 3.1416.

# 定义一个员工的集合
employee = {'武大郎': 7474, '潘金莲': 6868, '西门庆': 9898, '童铁蛋': 8888}
for name, salary in employee.items():
    # 8表示每列都显示8个宽度，数字宽度后面必须有d，字符串后面没有
    print(f'{name:8}===>{salary:8d}')

# !s str()强制转换
# !r repr()强制转换
# !a ascii()强制转换
name = '潘金莲'
s = f'the best salary is {name!s}'
print(s)  # the best salary is 潘金莲

s1 = f'the best salary is {name!r}'
print(s1)  # the best salary is '潘金莲'

s2 = f'the best salary is {name!a}'
print(s2)  # the best salary is '\u6f58\u91d1\u83b2'
