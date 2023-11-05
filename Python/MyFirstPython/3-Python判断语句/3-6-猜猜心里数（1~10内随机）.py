'''
要求：
1. 产生1~10随机一个数字
2. 有3次机会猜测，通过3层嵌套判断实现
3. 每次猜不中，提示大了还是小了

提示：
通过 
import random
num = random.randint(1, 10)
产生随机数字
'''

# 产生随机数
import random
num = random.randint(1, 10)

answer = int(input("猜猜我心里的数字："))
if answer != num:
    print("猜错了")
    # if answer < num:
    #     print("小了")
    # else:
    #     print("大了")
    answer = int(input("再猜一次："))
    if answer != num:
        print("还是猜错了")
        # if answer < num:
        #     print("小了")
        # else:
        #     print("大了")
        answer = int(input("最后再猜一次："))
        if answer != num:
            print("3次机会用完了，没有猜中")
        else:
            print("哦，最后猜对了")
    else:
        print("嗯，这次猜对了")
else:
    print("哇，一次就猜对了")

# 注释部分是提示大了还是小了，ctrl+/去除注释即可实现提示功能。