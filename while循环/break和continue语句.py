# 获取1到5的全部奇数
i = 1
while i < 11:
    print(i)
    if i == 5:
        break
    i += 2

# 获取1到10的全部奇数，5除外
j = -1
while j < 9:
    j = j + 2
    if j == 5:
        continue
    print(j)
