"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
0、整个项目做成3个.py文件，data_define.py，file_define.py，main（本程序）.py
1、设计一个类，完成数据的封装
2、设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
    (本例子提供了两种类型的元数据，一种是标准txt格式(仅以【,】分隔)，一种是json格式（字典）)
3、读取文件，生产数据对象
4、进行数据需求的逻辑计算（计算每日的销售额）
5、通过Pyecharts进行图形的绘制
"""
# 导入已构建好的模块
from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record

## 导入可视化相关模块
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 根据地址获取不同格式的数据
text_file_reader = TextFileReader("/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("/2011年2月销售数据JSON.txt")

# 使用FileReader中构建好的read_data()方法来预处理数据
jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = text_file_reader.read_data()
## 合并成一个list
all_data: list[Record] = jan_data + feb_data    # 列表可以直接用【+】加号合并

# 开始进行数据计算
## 想要的结果：{"2011-01-01": 1534, "2011-01-02": 300, "2011-01-03": 650}

data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():     # 这一行相当于定义date为key
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money
"""
说明
已预处理过的数据结构是这样的：{{"date", "order_id", money, "province"}, {"date", "order_id", money, "province"}...}
这是一个嵌套式的list，这种list转换成dict是最简单的，Python能自动对应生成【键值对】
而all_data是一个装载[Record]类型的list对象，Record本身是有对应属性的，可以直接使用【record.date】来调用Record的类属性。
"""

# 创建Bar()类的对象
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT)) # 调整参数：主题变浅色（蓝）

## 设定x，y轴的数据
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))  # 调整参数：不显示y轴上的（数据）标签
## 自定义设置标题样式
bar.set_global_opts(
    title_opts = TitleOpts(title="每日销售额")
)

## 渲染输出
bar.render("每日销售额柱状图.html")