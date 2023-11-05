# 1、定义一个列表，记录一批学生的年龄
list_age = [21, 25, 21, 23, 22, 20]
print(f"一批学生的年龄分别为：{list_age}")

# 2、追加一个31到列表尾部
list_age.append(31)
print(f"追加一位学生的年龄之后的列表为：{list_age}")

# 3、追加新一批学生的年龄，29，33，30到列表尾部
list_age_1 = [29, 33, 30]
list_age.extend(list_age_1)
print(f"追加新一批学生的年龄之后的列表为：{list_age}")

# 4、取出第一个元素（21）
element = list_age[0]
print(f"取出的元素是{element}")

# 5、取出最后一个元素(30)
## 最后一个元素可以用倒序下标"-1"
element = list_age[-1]
print(f"取出的元素是{element}")

# 查找元素31的下标位置
index = list_age.index(31)
print(f"元素\"31\"的下标为：{index}")