import json
import datetime

# 将json转换成字典
js = '{"name": "linna", "age": 18, "sex": "man"}'
# 将js转换成字典
resjs = json.loads(js)
print(resjs)
print(type(resjs))  # 可以看到已经转成字典
print(resjs['name'])  # linna
print(js)
print(type(js))

# 将python字典转换成json
dog = {
    'name': 'huahua',
    'age': 15,
    'sex': 'man'
}
# dumps()函数将字典转换成json
covert = json.dumps(dog)
print(covert)

# 将python对象转换成字符串
d = datetime.datetime.today()
birthday = str(d.date())
dog['birth'] = birthday
# 将字典转换成json打印输出
print(json.dumps(dog))
