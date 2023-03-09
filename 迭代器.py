mytuple = ("apple", "banana", "cherry")
myiter = iter(mytuple)
print(next(myiter))  # apple
print(next(myiter))  # banana

# 全局变量
x = 100


def myfunction():
    # 使用global之后该变量是全局变量
    global x
    x = 200
    print(x)


myfunction()
print(x)
