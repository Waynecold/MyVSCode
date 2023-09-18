'''
要求：
1. 使用for循环
2. 遍历字符串："itheima is a brand of itcast"
3. 统计有多少个英文字母"a"
'''

name = "itheima is a brand of itcast"
count = 0
for x in name:
    if x == "a":
        count += 1
print(f"itheima is a brand of itcast总共含有{count}个字母a。")