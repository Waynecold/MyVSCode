"""
单继承演示
"""

class Phone:                    # 第一代类的功能
    IMEI = None
    producer = "Huawei"             # 生产商

    def call_by_4G(self):
        print("4G通话")

class Phone2023(Phone):          # 2023款包含第一代的所有功能
    face_id = "10010"            # 新的属性和方法

    def call_by_5G(self):
        print("2023新功能，5G通话")

print("1、单继承演示")
phone = Phone2023()
print(phone.producer)               # 调用旧的属性
phone.call_by_4G()                  # 调用旧的方法
phone.call_by_5G()                  # 调用新的方法

"""
多继承演示
"""

class NFCReader:                   # NFC功能
    nft_type = "第五代"
    producer = "xiaomi"             # nfc生产商

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoteControl:                # 红外遥控功能
    re_type = "红外遥控"

    def control(self):
        print("新添红外遥控功能")

class MyPhone(Phone2023, NFCReader, RemoteControl):
    pass                            # pass关键字，使类空内容不报错

print("2、多继承演示")
phone = MyPhone()
phone.call_by_4G()
phone.call_by_5G()
print(phone.producer)               # 成员属性重名了，按继承顺序排列优先级
phone.read_card()
phone.control()
