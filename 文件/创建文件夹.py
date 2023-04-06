import os

save_path = r'D:\python文件学习'
if os.path.exists(save_path):
    print(f'文件夹{save_path}已经存在')
else:
    print(f'文件夹{save_path}不存在可以创建')
    os.mkdir(save_path)
