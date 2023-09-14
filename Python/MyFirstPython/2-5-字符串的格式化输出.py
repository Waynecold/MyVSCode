# 1 使用%s拼接输出
name = "Wayne"
message = "你好，%s。" % name
print(message)

# 2 多个数字和字符串的拼接输出
weather = "小到中雨"
date = 14
month = 9
#原本是数字类型，%s转换成字符串类型
message = "今天是%s月%s日，今天的天气是%s。" % (month, date, weather)
print(message)

# 3 数字的修饰符m.n
num1 = 11
num2 = 11.345
print("数字11设置宽度限制5，结果是：%5d" % num1)
print("数字11设置宽度限制1，结果是：%1d" % num1)
print("数字11设置宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字11设置宽度限制不限制，小数精度2，结果是：%.2f" % num2)

# 4 字符串快速格式化：f"(占位)"
weather = "小到中雨"
date = 14
month = 9
print(f"今天是{month}月{date}日，今天的天气{weather}。")