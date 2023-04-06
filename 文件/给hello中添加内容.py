f = open('D:\python文件学习\hello1.txt', 'w', encoding='utf-8')
f.write('心上人是心上人\n')
f.write('有什么办法呢\n')
f.close()
f = open('D:\python文件学习\hello1.txt', 'r', encoding='utf-8')
print(f.read())
# 参数x，如果文件存在则返回错误
f = open('D:\python文件学习\hello1.txt', 'x', encoding='utf-8')
