# 定义
str1 = "My name is Wayne"
print(str1)

# 下标取值
value1 = str1[1]
value2 = str1[2]
value3 = str1[3]
print(f"str1中下标是1的值是：{value1}")
print(f"str1中下标是2的值是：{value2}")
print(f"str1中下标是3的值是：{value3}")

# 修改（无效）
# str1[1] = "fix"

# index查询
value = str1.index("Wayne")
print(f"\"Wayne\"所在的下标是：{value}")

# 字符串的操作
## replace替代
str1_fix_1 = str1.replace("ame", "ephew")
print(f"原字符串{str1}经过replace替换之后变成了{str1_fix_1}")

## (空格处)split拆分 经拆分后，字符串类型变为列表
str1_fix_2 = str1.split(" ") # 此处为空格" "，其他字符亦然
print(f"原字符串{str1}经过split拆分之后变成了{str1_fix_2}，类型是{type(str1_fix_2)}")

## strip去掉前后空格
str2 = "    666that is amazing666 "
str2_fix_1 = str2.strip() # 不填默认去空格
print(f"字符串[{str2}]经过strip之后，得到[{str2_fix_1}]")

str2_fix_2 = str2_fix_1.strip("666") # 去掉"i"前后的所有字符
print(f"字符串[{str2_fix_1}]经过strip掉\"666\"之后，得到[{str2_fix_2}]")

## count统计字符出现的次数
count = str2_fix_2.count("a")
print(f"字符串{str2_fix_2}的\"a\"出现的次数为：{count}")

## len()统计字符串的长度
num = len(str2_fix_2)
print(f"字符串{str2_fix_2}的长度是{num}")