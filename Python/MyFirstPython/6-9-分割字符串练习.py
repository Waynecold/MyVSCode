# 定义一个字符串
str = "itheima itcast boxuegu"

# 统计有多少个"it"字符
count = str.count("it")
print(f"字符串{str}中有{count}个\"it\"字符")

# 将字符串内的空格，全部替换为字符："|"
str1 = str.replace(" ", "|")
print(f"原字符串{str}被替换为{str1}")

# 按照"|"分割，得到新的列表
list = str1.split("|")
print(f"原字符串{str1}被分割为列表{list}")