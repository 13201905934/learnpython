f = open('D:\python文件学习\\real.txt', 'r', encoding='utf-8')
print(f.readline())
print(f.readline())
print(f.readline())

# 利用for循环读取读取文件数据
for c in f:
    print(c)
