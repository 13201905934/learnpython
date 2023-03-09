try:
    print("hello")
except:
    print("something is wrong")
else:
    print("nothing is wrong")
x = -1
if x < 0:
    raise Exception("扔的就是-1你")

y = "hi"
if not type(y) is int:
    raise TypeError("非整数")
