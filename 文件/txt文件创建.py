f = open('D:\python文件学习\hello.txt', 'w')
f.write('春眠不觉晓，处处闻啼鸟')
f.close()
f1 = open('D:\python文件学习\hello.txt', 'r')
x = f1.read()
print(x)
