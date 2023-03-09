# 正则表达式
import re

txt = "china is a great country"
x = re.search("^china.*country$", txt)
print(x)
z = re.findall("a", txt)  # ['a', 'a', 'a']
print(z)
