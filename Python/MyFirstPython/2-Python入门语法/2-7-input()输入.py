print("请告诉我你是谁？")
name = input()
print("我知道了，你是%s。" % name)

# 进一步优雅
name = input("请告诉我你是谁？")
print("我知道了，你是%s。" % name)

# 输入数字类型
num = input("请输入银行卡密码：")
print("你的银行卡密码原始类型是：", type(num))
# 从结果可以看出，输入的类型是固定字符串类型

# 于是需要进行数据转换
num = int(num)
print("你的银行卡密码转换后的类型是：", type(num))