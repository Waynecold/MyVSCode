import json

# 准备列表，列表内元素是字典，将转换成JSON
data = [{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]
json_str = json.dumps(data, ensure_ascii = False) # 不以ascii编码转换中文
print(type(json_str))
print(json_str)

# 准备字典，将字典转换为JSON
d = {"name":"周杰轮", "addr":"台北"}
json_str = json.dumps(d, ensure_ascii = False)
print(type(json_str))
print(json_str)

# 将JSON字符串转换为Python数据类型（列表）
s = '[{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]'
l = json.loads(s)
print(type(l))
print(l)

# 将JSON字符串转换成Python数据类型（字典）
s = '{"name": "周杰轮", "addr":"台北"}'
d = json.loads(s)
print(type(d))
print(d)
