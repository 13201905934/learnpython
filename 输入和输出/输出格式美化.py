year = 2018
event = '中美贸易战'
# 格式化的字符串是以f或F开始，后面紧跟一个或三个引号括起来的字符串，在此字符串中可以在大括号内部使用python表达式
print(f'{year}年{event}')

# 将格式化的字符串也可以放在一个变量中
p = f'{year}年{event}'
print(p)

revenue = 380
cost = 330
net_profit_margin = (revenue - cost) / revenue
# {:3}->指的参数revenue显示宽度为3位  {:2.2%}->net_profit_margin以百分数显示，整数和小数都是两位
print('{:3}万元的年收入，其利润为{:2.2%}'.format(revenue, net_profit_margin))

# 定义一个字符串 repr与str区别
s = 'Kelble is the king in my family.\n'
print(repr(s))  # 'Kelble is the king in my family.\n'
print(str(s))  # Kelble is the king in my family.
