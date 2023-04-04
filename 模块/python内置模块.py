import platform
import moka

print(platform.system())  # Windows
print(dir(platform))  # dir 列出模块中所有函数和变量名称
for i in dir(platform):
    print(i)
print(dir(moka))
for i in dir(moka):
    print(i)
