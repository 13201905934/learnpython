def fibnacci(num):
    if num <= 1:
        return num
    elif num > 1:
        return fibnacci(num - 1) + fibnacci(num - 2)


numbers = int(input('你想要多少个斐波那契数列：'))
if numbers < 0:
    print("请输入一个大于0的数")
else:
    for i in range(numbers):
        print(fibnacci(i))
