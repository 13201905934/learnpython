n = int(input("please enter a natural number: "))
i = 1
factory = 1
if n <= 0:
    print("请输入一个大于零的整数")

else:
    while i <= n:
        factory = factory * i
        i = i + 1
    print(factory)

m = int(input("请输入一个整数"))
j = 1
p = 1
if m <= 0:
    print('请输入一个大于零的整数')
else:
    while j <= m:
        p = p * j
        j += 1
    print(p)
