# 定义水果字典
price = {"苹果": 10, "香蕉": 15, "橘子": 6, "石榴": 7}

# 打印今日份水果价格
print("今日份水果价格：")
for fruit in price:
    print("%s今日%d元" % (fruit, price[fruit]))
print(" ")

n = int(input("请输入你想购买的水果种类数量"))

sum_price = 0

for i in range(0, n):
    fruits = input("请输入购买的水果%d名称" % (i + 1))
    num = int(input("请输入购买的水果%d数量" % (i + 1)))
    # 判断水果是否存在
    if fruit in price.keys():
        sum_price += num * price[fruit]
print("总价格为%d" % (sum_price))
