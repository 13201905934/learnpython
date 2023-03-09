# fromkeys使用
d = {}
d1 = d.fromkeys(("name", "age"))  # {'name': None, 'age': None}
d2 = d.fromkeys(("name", "age"), 9)  # {'name': 9, 'age': 9}

print(d1)
print(d2)

# pop使用
m = {
    "name": "qiangwengang",
    "age": "24"
}
res = m.pop("name")
print(res)  # qiangwengang

# popitem删除字典中最后一项
m1 = {
    "name": "qiangwengang",
    "age": "24"
}
res2 = m1.popitem()
print(res2)  # ('age', '24')
print(m1)  # {'name': 'qiangwengang'}

# setdefault 添加键值，若存在就不添加
m1.setdefault("sex", "man")
print(m1)  # {'name': 'qiangwengang', 'sex': 'man'}
