'''
要求：表白100天
每天送10支玫瑰
最后表白成功
使用for循环
'''
x = 0
for x in range(1, 101):
    print(f"第{x}天，准备表白💪")
    for y in range(1, 11):
        print(f"给小美送到第{y}支🌹玫瑰花")
    print("💕小美我喜欢你")
print(f"第{x}天，表白成功❗")