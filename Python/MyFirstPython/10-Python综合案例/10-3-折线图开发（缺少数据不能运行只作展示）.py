# 这里的示例只展示方法，数据并不存在，！！！不能运行此程序！！！
import json
from pyecharts.charts import Line # 导包，导入折线图功能
from pyecharts.options import TitleOpts, LabelOpts # 导入标题设置

# 处理数据
f_us = open("D:/Documents/MyVSCode/Python/MyFirstPython/10-Python综合案例/10-3-1-美国.txt", "r", encoding="utf-8")
us_data = f_us.read()

f_jp = open("D:/Documents/MyVSCode/Python/MyFirstPython/10-Python综合案例/10-3-1-美国.txt", "r", encoding="utf-8")
jp_data = f_jp.read()

f_in = open("D:/Documents/MyVSCode/Python/MyFirstPython/10-Python综合案例/10-3-1-美国.txt", "r", encoding="utf-8")
in_data = f_in.read()

## .replace去掉不合JSON规范的结尾
us_data = us_data.replace("jsonp_***", "")
jp_data = jp_data.replace("jsonp_***", "")
in_data = in_data.replace("jsonp_***", "")

## 去掉不合JSON规范的结尾
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# JSON转到Python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 获取日期数据，用于x轴，取2020年（到314下标结束）
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]

# 获取确认数据，用于y轴，取2020年（到314下标结束）
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 生成图表
## 构建折线图对象
line = Line()
## 添加x轴数据
line.add_xaxis(us_x_data) #x轴共用，只取一份即可
## 添加y轴数据
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False)) # label设置不显示
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

# 设置全局选项
line.set_global_opts(
    # 标题设置
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%")

)

# 调用render方法，生成图表
line.render()

# 关闭文件对象
f_us.close()
f_jp.close()
f_in.close()