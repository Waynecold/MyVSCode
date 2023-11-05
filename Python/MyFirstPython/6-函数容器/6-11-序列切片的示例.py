'''
有字符串"万过薪月，员序程马黑来，nohtyP学"
1、使用学过的任何方法，得到："黑马程序员"
提示：
# 1、倒序字符串，切片取出，或者切片取出然后倒序
# 2、split分隔"，"，replace替换"来"为空，倒序字符串
'''

str = "万过薪月，员序程马黑来，nohtyP学"

# num3 = len(str)
# print(f"字符串的长度是{num3}")
# ## 得到19，即正序[0, 18]或倒序[-1, -19]

# 1

## 先倒序再取值
str1 = str[::-1]

index1 = str1.index("黑")
index2 = str1.index("员")
print(f"倒序黑字的下标为{index1}，员的下标为{index2}") # 得到9，13
result1 = str1[9:13+1]
print(f"方法1：{result1}")

# 2

## 先取出再倒序
index1 = str.index("员")
index2 = str.index("黑")
print(f"正序黑字的下标为{index1}，员的下标为{index2}") # 得到5，9
str2 = str[5:9+1]
result2_1 = str2[::-1]
print(f"方法2.1：{result2_1}")

## 整合写法
result2_2 = str[5:9+1][::-1]
print(f"方法2.2：{result2_2}")

# 3

## 先split分割
str3 = str.split("，")
## 取split的中间部分
str3_1 = str3[1]
## 再replace替换
str3_2 = str3_1.replace("来", "")
## 取倒序
result3_1 = str3_2[::-1]
print(f"方法3.1：{result3_1}")

## 整合写法
result3_2 = str.split("，")[1].replace("来", "")[::-1]
print(f"方法3.2：{result3_2}")

# 总结：
# 方法3不需要考虑下标，相对简洁，但要求对序列整体有充分把握；
# 方法1和2的情况适合，序列很大不能完全掌握，只有模糊印象，需要下标来定位需要改动的位置