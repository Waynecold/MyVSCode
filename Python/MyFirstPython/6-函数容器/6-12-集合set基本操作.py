# 定义集合
set1 = {"hello", "world", "nihao", "shijie", "hello", "world", "nihao", "shijie"}
set1_empty = set()  # 定义空集合
print(f"1、set1的内容是：{set1}，类型是：{type(set1)}")
print(f"1.1、set1_empty的内容是：{set1_empty}，类型是：{type(set1_empty)}")

# 添加新元素
set1.add("Python")
set1.add("nihao")   # 添加已有的元素不会重复
print(f"2、set1添加元素之后的结果是：{set1}")

# 移除元素
set1.remove("world")
print(f"3、set1移除元素之后的结果是：{set1}")

# 随机取出一个元素
set1 = {"hello", "world", "nihao", "shijie"}
element = set1.pop()
print(f"4、集合被取出元素\'{element}\'后得到的集合是{set1}")

# 清空集合
set1.clear()
print(f"5、集合被清空后得到的集合是{set1}")

# 取出集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(f"6.1、取差集之后的结果：{set3}")
print(f"6.2、取差集之后set1的结果：{set1}")
print(f"6.3、取差集之后set2的结果：{set2}")
# 得到结果是，set3为[2, 3]，set1和set2原集合不变

## 消除集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(f"7.1、消除差集之后set1的结果：{set1}")
print(f"7.2、消除差集之后set2的结果：{set2}")
# set1中消除set2重复的元素后，set1变成[2, 3]，而set2不变

## 合并集合
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"8.1、合并结果为{set3}")
print(f"8.2、合并后set1为{set1}")
print(f"8.3、合并后set2为{set2}")
# 合并后得到新的集合，原集合均不变

# 统计集合元素的数量
set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6}
count1 = len(set1)
count2 = len(set2)
print(f"9.1、集合set1内的元素数量为：{count1}")
print(f"9.2、集合set2内的元素数量为：{count2}")
# 结果都是6，因为集合的最后都是去重的

# 集合的遍历
## 集合不支持下标索引，不支持while循环
set1 = {1, 2, 3, 4, 5, 6}
for element in set1:
    print(f"10、集合的元素有：{element}")