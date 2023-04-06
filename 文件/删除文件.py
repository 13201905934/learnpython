import os

thing = 'D:\python文件学习\\th.txt'
f = open('D:\python文件学习\\th.txt', 'w', encoding='utf-8')
f.close()
# 删除'D:\python文件学习\\th.txt',删除之前检查是否存在
if os.path.exists(thing):
    os.remove(thing)
else:
    print("文件不存在")
