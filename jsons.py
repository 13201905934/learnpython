# 导入json模块
import json

# json
x = '{"name":"Bill","age":63,"city":"chengdu"}'
# 解析x 注意文件名称不能和json一样，且使用loads方法
y = json.loads(x)
print(y)

# 将python转换成json
person = {
    "name": "changChen",
    "age": 18,
    "sex": "man"
}
# 使用json的dump()方法将person转换成json格式
z = json.dumps(person)
print(z)

lover = {
    "name": "lover",
    "age": 25,
    "sex": "women"
}

print(json.dumps(lover))

y1 = '{"name":"qiangwengang","age":25}'

g1 = json.loads(y1)
print(g1)
