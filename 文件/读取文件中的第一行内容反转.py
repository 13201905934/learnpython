def res_str(s):
    return s[::-1]


# +' 模式，更新文件，同时支持读取和写入；

# '+' 模式不能单独使用，需要配合 'r'、'w'模式一起使用；

# 'r+' 模式打开文件，但不清空内容，支持读取、写入、修改文件指针；

# 'w+'模式打开文件，清空内容，也支持读取、写入、修改文件指针
s = '春眠不觉晓'
f = open('D:\python文件学习\\反转文件.txt', 'r+', encoding='utf-8')
f.write(s)
f.close()
f1 = open('D:\python文件学习\\反转文件.txt', 'r+', encoding='utf-8')
s1 = f1.readline()
s2 = res_str(s1)
f1.write(s2 + '\n')
f1.close()