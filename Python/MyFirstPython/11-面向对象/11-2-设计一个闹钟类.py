# 设计一个闹钟类
class Clock:
    id = None       # 序列化
    price = None    # 价格

    def ring(self):
        import winsound
        winsound.Beep(2000, 1000)   # (频率，持续时间)

# 构建2个闹钟对象并让其工作
clock1 = Clock()
clock1.id = "003032" # type: ignore
clock1.price = 19.99 # type: ignore
print(f"闹钟ID：{clock1.id}，价格：{clock1.price}")
clock1.ring()

clock2 = Clock()
clock2.id = "003033" # type: ignore
clock2.price = 21.99 # type: ignore
print(f"闹钟ID：{clock2.id}，价格：{clock2.price}")
clock2.ring()