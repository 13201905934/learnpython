# 有时文本的一部分是你无法控制的，也许它们来自数据库或用户输入？

# 要控制此类值，请在文本中添加占位符（花括号 {}），然后通过 format() 方法运行值
x = 100
txt = "the price is {} dollar"  # the price is 100 dollar
print(txt.format(x))

text = "I have {cs} apple and {zs} banana"
print(text.format(cs="2", zs="4"))  # I have 2 apple and 4 banana

# 字符串拼接
a = "你好啊"
b = "强文刚"
c = ",".join((a, b))  # 你好啊,强文刚
print(c)

d = "大家好，我叫{}，今年{}，性别{}".format("qiangwengang", "24", "nan")
print(d)

# 字符串查找，跟字符串统计，如果有多个要找到的字符串，则返回第一次出现的下标

m = "helloWorld"
f = m.find("o")
print(f)  # 4
g = m.count("o")
print(g)  # 2
# 字符串替换
s1 = "python to muzhou"
# 1代表替换一次，不写默认其全替换0
res = s1.replace("o", "TT", 1)
print(res)  # pythTTn to muzhou

# 字符串大小写转换
res3 = s1.upper()
print(res3)  # PYTHON TO MUZHOU
res4 = s1.lower()
print(res4)  # python to muzhou

# 字符串分割和去除字符串首尾
res5 = "dsdkkkkkdsdsw"  # ['dsd', '', '', '', '', 'dsdsw']
print(res5.split("k"))
res6 = "6666jis66"
print(res6.strip("6"))  # jis

# 字符串格式化输出  %s占位符
res8 = "我%s你" % ("爱")
print(res8)
res9 = "我的成绩是%d" % (100)  # 我的成绩是100
print(res9)

res10 = "我的身高是%f" % (180)  # 我的身高是180.000000

print(res10)

# F表达式
name = "qiangwengang"
sex = "man"
res11 = F"我的名字是{name},性别{sex}"  # 我的名字是qiangwengang,性别man

print(res11)

# 小数精确
s = 3.1415
res12 = "今天的橘子{:.2f}一斤，很甜".format(s)  # 今天的橘子3.14一斤，很甜

print(res12)

# 转换百分比
s = 0.123
print("百分比{:.2%}".format(s))  # 百分比12.30%
