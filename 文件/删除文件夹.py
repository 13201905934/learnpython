import os

folder_name = input('请输入要删除文件夹： ')
# 删除空文件夹
if os.path.exists(folder_name):
    os.rmdir(folder_name)
else:
    print("输入要删除的文件不存在！")
