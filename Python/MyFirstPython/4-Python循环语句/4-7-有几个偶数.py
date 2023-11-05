'''
要求：
1、结合range()语句和for循环
2、求范围在1到100（不含100）的序列中，遍历它
3、统计有多少个偶数
'''

num = 100
count = 0
for x in range(1, num): # 遍历1-100
    if x % 2 == 0:
        count += 1
print(f"1到100（不含100）范围内，有{count}个偶数")