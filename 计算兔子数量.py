rabbit = 3  # 兔子初始数量

print("请输入N的值")

N = int(input())

for i in range(0, N):
    rabbit = rabbit * 2

print("%d年后,兔子数量是%d只" % (N, rabbit))
