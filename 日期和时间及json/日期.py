import datetime

# 显示当前时间
d = datetime.datetime.now()
print(d)
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)
# 查看datetime的全部属性
print(dir(datetime))

# 设置时间
d1 = datetime.date(2019, 2, 1)
print(d1)
# 用time创建时间
t = datetime.time(13, 13, 21)
print(t)
# 时间格式化
print(d.strftime('%a'))  # Fri
print(d.strftime('%A'))  # Friday
# 数字星期几
print(d.strftime('%w'))  # 5
# 具体几号
print(d.strftime('%d'))  # 07
# 月份
print(d.strftime('%b'))  # Apr
# 数字形式月份
print(d.strftime('%m'))  # 04
# 数字形式确定几点
print(d.strftime('%I'))  # 09
# 今年的第多少周
print(d.strftime('%W'))  # 14
# 具体时间信息
print(d.strftime('%c'))  # Fri Apr  7 21:53:37 2023

# 几时几分几秒
print(d.strftime('%X'))  # 21:54:26
