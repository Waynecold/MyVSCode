# 定义一个类，内含有私有成员变量和私有成员方法

class Phone:
    __current_voltage = 0.5    # 当前电压

    def __keep_single_core(self):       # 私有方法自身无法被类对象直接调用
        print("让CPU以单核模式运行")
    
    def call_by_5g(self):               # 这成员方法使用了私有方法
        if self.__current_voltage >= 1:
            print("5G通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5G通话，已设置为单核运行进行省电")

phone = Phone()
# print(phone.__current_voltage)    # >> 报错
# phone.__keep_single_core()

phone.call_by_5g()                  # >> 成功调用方法