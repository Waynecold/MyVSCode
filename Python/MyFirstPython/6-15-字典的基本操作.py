dict1 = {"wang": 99, "zhou": 88, "lin": 77}
print(f"0、原字典的内容是{dict1}")

# 新增元素
dict1["zhang"] = 66
print(f"1、新增元素后，结果是{dict1}")

# 更新元素
dict1["zhou"] = 33
print(f"2、字典经过更新后，结果是{dict1}")

# 取出并删除元素
score = dict1.pop("zhou")
print(f"3、字典取出zhou的分数{score}后，字典的内容结果是{dict1}")

# 清空元素
dict1.clear()
print(f"4、字典被清空后，结果为：{dict1}")

#获取全部的Key
dict1 = {"wang": 99, "zhou": 88, "lin": 77}
keys = dict1.keys()
print(f"5、字典全部的Key有{keys}")

# 遍历字典
for key in keys:
    print(f"6.1、字典的Key是{key}，Value是{dict1[key]}")

for key in dict1:
    print(f"6.2、字典的Key是{key}，Value是{dict1[key]}")

# 统计字典内的元素数量
num = len(dict1)
print(f"7、字典中的元素数量为{num}")