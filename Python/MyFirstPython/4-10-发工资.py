'''
1、某公司账户余额1W元，给20个员工发工资，每人1000元
2、按员工的绩效分（1-10）（随机生成），低于5，不发工资，下一位
3、如果余额不足了，终止发工资

提示：
使用continue跳过员工，break直接结束发工资
随即数使用：
import random
num = random.randint(1, 10)
'''

'''
以发放人数为循环，再以余额限制终止的写法
'''

money = 10000
employee = 20

for i in range(1, employee + 1):

    # 先判断余额
    if money <= 0:
        print("余额不足了💁‍♂️，下个月领取吧。")
        break 
 
    # 获取绩效分
    import random
    score = random.randint(1, 10)

    num = i
    # 判断绩效分，不满足，跳过，进入下一循环
    if score < 5:
        print(f"💼员工{i}，绩效分{score}，低于5，不发工资，下一位。")
        continue # 此处continue其实可以换成else语句包裹下面👇的代码块

    # 绩效分通过才发1000
    money -= 1000
    print(f"💼员工{i}，发放工资1000元，账户余额还剩余{money}。")
print("✨本轮工资发放完毕🎉")