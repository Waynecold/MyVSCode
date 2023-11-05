# 定义列表
my_list = ["hello", "name", "wayne"]

# 1 - 查询某元素的下标索引
index = my_list.index("name")
print(f"1、name在my_list列表中的下标索引是{index}")

# 1.1 - 如果查找的元素不存在，会报错，显示
# index = my_list.index("bye")
# print(f"1.1、"bye"在列表中的下标索引是{index}")

# 2 - 修改特定下标索引的值
my_list[0] = "my"
print(f"2、元素的值被修改后，列表变为：{my_list}")

# 3 - 指定下标位置插入新元素
my_list.insert(2, "is")
print(f"3、通过.insert插入新元素后，列表变为：{my_list}")

# 4 - 把新元素追加到列表尾部
my_list.append("nice to meet you")
print(f"4、通过.append追加新元素后，列表变为：{my_list}")

# 5 - 把多个新元素追加到列表尾部
my_list2 = ["how", "are", "you"]
my_list.extend(my_list2)
print(f"5、通过.extend追加一批新元素后，列表变为：{my_list}")

# 6 - 删除指定下标的元素
## 6.1 - del list[#]
my_list = ["hello", "name", "wayne"]
del my_list[1]
print(f"6.1、删除my_list中第2个元素后，列表变为：{my_list}")

## 6.2 - list.pop(#)
my_list = ["hello", "name", "wayne"]
element = my_list.pop(2)
print(f"6.2、通过.pop方法取出元素{element}后，my_list变为：{my_list}")

## 6.3 - list.remove(#)
my_list = ["hello", "world", "hello", "wayne"]
my_list.remove("hello")
print(f"6.3、通过.remove删除指定元素后，列表变为：{my_list}")

# 7 - 清空列表内容
my_list.clear()
print(f"7、通过.clear删除指定元素后，列表变为：{my_list}")

# 8 - 统计列表中元素的数量
## 8.1 - 单个指定元素
my_list = ["hello", "world", "hello", "wayne"]
count = my_list.count("hello")
print(f"8.1、通过.count统计\"hello\"元素的个数为：{count}")

## 8.2 - 全部元素
my_list = ["hello", "world", "hello", "wayne"]
count = len(my_list)
print(f"8.2、通过.count统计全部元素的个数为：{count}")