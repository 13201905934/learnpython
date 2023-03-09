def abc(a, *, c, d):
    print(a)
    print(d)
    print(c)


# abc(100, 200, 300)这样写会报错
abc(100, c=900, d=20)  # 必须得这种形式写


def ac(a, *b):  # *b代表一个元组，收集未匹配的元素 或者可以把*b写成*args 可变参数
    print(a)
    print(b)


ac(100)  # 100 ()
ac(100, 200, 300, 400)  # (200, 300, 400)都放在元组里了


def av(a, **kwargs):  # **kwargs指向字典,收集未匹配的元素
    print(a)
    print(kwargs)


av(100, x=100, y=200)  # {'x': 100, 'y': 200}

# 参数解包
a = [1, 2, 3]


def fun(a, b, c):
    print(a)
    print(b)
    print(c)


fun(*a)

# 字典解析

d = {
    "a": "qiangwengang",  # 键名要和参数名一致
    "b": "24",
    "c": "ko"
}
fun(**d)  # 拿到value qiangwengang 24 ko
