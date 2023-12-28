"""
设计一个手机类，内部包含：
1、私有成员变量：__is_5G_enable，类型bool，True表示开启5G，False表示关闭5G
2、私有成员方法：__check_5G()，用来判断私有成员__is_5G_enable的值：
    - True，打印输出：5G开启
    - False，打印输出：5G关闭，使用4G网络
3、公开成员方法，call_by_5G()，调用它执行：
    - 调用私有成员方法：__check_5G()，判断5G网络状态
    - 打印输出：正在通话中
4、运行结果：5G关闭，使用4G网络
            正在通话中
"""

class Phone:                                # 创建类
    __is_5G_enable = False  # 5G关闭        # 私有变量

    def __check_5G(self):                   # 私有方法
        if self.__is_5G_enable:
            print("5G开启")
        else:
            print("5G关闭，使用4G网络")
    
    def call_by_5g(self):                   # （正常）成员方法
        self.__check_5G()
        print("正在通话中")

phone = Phone()                             # 通过类来创建对象
phone.call_by_5g()                          # 调用类的成员方法