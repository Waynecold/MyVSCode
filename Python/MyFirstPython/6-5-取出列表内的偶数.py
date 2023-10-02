#定义一个列表
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 遍历列表，取出列表中的偶数，并存入一个新的列表对象中
## while循环
num2 = []
index = 0
while index < len(num):
    element = num[index]
    if (element % 2) == 0:
        num2.append(element)
    index += 1
print(f"通过while循环，从列表：{num}中取出偶数，组成新列表：{num2}")

## for循环
num3 = list()
for element in num:
    if element % 2 == 0:
        num3.append(element)
print(f"通过for循环，从列表：{num}中取出偶数，组成新列表：{num3}")