def rev_str(str):
    return list(dict.fromkeys(str))


num = []
for j in range(10, 101, 10):
    # 将10个数添加到num中
    num.append(j)
    # j能除尽20再添加一次
    if j % 20 == 0:
        num.append(j)
print(num)  # [10, 20, 20, 30, 40, 40, 50, 60, 60, 70, 80, 80, 90, 100, 100]
# 对其反转
rev_num = num[::-1]
print(rev_num)  # [100, 100, 90, 80, 80, 70, 60, 60, 50, 40, 40, 30, 20, 20, 10]
# 去重
rev_num1 = rev_str(rev_num)
print(rev_num1)  # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
