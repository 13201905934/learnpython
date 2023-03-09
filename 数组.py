import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
# 检查numpy版本
print(np.__version__)  # 1.23.5

# NumPy 用于处理数组。 NumPy 中的数组对象称为 ndarray。

# 我们可以使用 array() 函数创建一个 NumPy ndarray 对象
print(type(arr))  # <class 'numpy.ndarray'>

# 要创建 ndarray，我们可以将列表、元组或任何类似数组的对象传递给 array() 方法，然后它将被转换为 ndarray
arr1 = np.array((1, 2, 3, 4, 5))
print(arr1)
print(type(arr1))

# 0-D数组
arr2 = np.array(66)
print(arr2)  # 66
print("几维数组：", arr2.ndim)

# 1-D数组
arr3 = np.array([1, 2, 3])
# 裁切一维数组,最后的1表示步长
print("裁切一维数组:")  # [1]
print(arr3[0:1:1])
print(arr3)
print("几维数组：", arr3.ndim)

# 2-D数组
print("二维数组：")
arr4 = np.array([[1, 2], [2, 3], [5, 6], [6, 7]])
print(arr4)
print("裁切二维数组")
print(arr4[1, 0:1])  # [2]
print("返回四个1-D元素索引1：")
print(arr4[0:, 1])  # [2 3 6 7]
print("返回四个1-D元素,每个元素的值：")
print(arr4[0:, 0:])

print("几维数组：", arr4.ndim)
# 查看数组的形状，用shape
print(arr4.shape)  # (4, 2) 有四个1-D 每一个1-D里有两个元素
print(arr4.size)  # 8 有八个元素
# 3-D数组
print("三维数组：")
arr5 = np.array([[[1, 2], [4, 5]], [[6, 7], [8, 9]]])
print(arr5)
print(arr5.shape)  # (1,4,2)
print("几维数组：", arr5.ndim)
c = input("what is your name?")
if c == "qiangwengang":
    print("welcome to here")
else:
    print("do not look me!")
# 创建更高维度的数组
arr6 = np.array([1, 2, 3, 4], ndmin=5)
print(arr6)
