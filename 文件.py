# 如需在 Python 中创建新文件，请使用 open() 方法，并使用以下参数之一：

# "x" - 创建 - 将创建一个文件，如果文件存在则返回错误
# "a" - 追加 - 如果指定的文件不存在，将创建一个文件
# "w" - 写入 - 如果指定的文件不存在，将创建一个文件

# f = open("D:\\pythonFile\\hello.txt", "x") 创建hello.txt
f = open("D:\\pythonFile\\hello.txt", "a")
f.write("人的一生是困难的")
f.close()
# 写入后读取
f = open("D:\\pythonFile\\hello.txt", "r")
print(f.read())
