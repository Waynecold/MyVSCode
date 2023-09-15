'''动物园入场判断'''
# if int(input("你的身高是多少：")) > 120:
#     print("身高超出限制，不可以免费。")
#     print("但是，如果VIP等级大于3，可以免费。")
#     if int(input("你的VIP等级是多少：")) > 3:
#         print("恭喜你，VIP等级达标，可以免费。")
#     else:
#         print("Sorry，你需要买票10元。")
# else:
#     print("欢迎小朋友，可以免费游玩。")

'''入职福利领取'''
# 获取年龄，入职年数，级别等信息，优先级：age>year||level
age = 20
year = 1
level = 5

if age > 18:
    print("成年人")
    if age < 30:
        print("年龄符合")
        if year > 2:
            print("入职年数符合")
        elif level > 3:
            print("级别高于3，符合")
        else:
            print("入职时间和级别都不符合")
    else: 
        print("年龄太大")
else:
    print("年龄太小")
