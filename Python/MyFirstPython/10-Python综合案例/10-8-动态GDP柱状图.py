'''
列表sort方法排序，用于对传入参数前先进行一定的排序
'''
# 带名函数形式
my_list = [["a", 33], ["b", 55], ["c", 11]]

# 定义排序方法
def choose_sort_key(element):
    return element[1]

my_list.sort(key=choose_sort_key)
print(my_list)

# 另一种，使用lambda匿名一次函数的方法
my_list.sort(key=lambda element: element[1], reverse=True) #reverse代表倒序
print(my_list)

'''
演示GDP动态柱状图的开发（缺少数据）
'''

from pyecharts.charts import Bar, Timeline
from pyecharts.options import *

# 读取数据
f = open("/MyVSCode/Python/MyFirstPython/10-Python综合案例/1960-2019全球GDP数据.cvs", "r", encoding="GB2312")
data_lines = f.readlines()

# 关闭文件
f.close()

# 删除无关数据（如删除第一条，下标为[0]）
data_lines.pop(0)

# 将数据转换为字典存储，格式为：
# {年份:[[国家, GDP], [国家, GDP], ...], 年份:[[国家, GDP], [国家, GDP], ...], ...}

# 定义字典对象
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0]) # 以逗号为分隔，取第一个数据[0]，并转换成数字int，得到年份
    country = line.split(",")[1] # 取得第二个数据，得到国家
    gdp = float(line.split(",")[2]) # 有科学计数法的数据可以统一转换成浮点数，再取得GDP数据

    # 捕获异常
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# 创建时间线对象
timeline = Timeline()

# 年份排序
# 获取全部的Key-年份的范围
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    # 按照相同年份的list中的第二个数据排序-GDP，倒序
    data_dict[year].sort(lambda element: element[1], reversed=True)
    # 取出本年份前就名的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    # 添加x，y轴数据
    for country_gdp in year_data:
        x_data.append(country_gdp[0]) # x轴添加国家
        y_data.append(country_gdp[1]) # x轴添加GDP
    
    # 构建柱状图，需要导包
    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP（亿）", y_data, label_opts=LabelOpts(position="right"))
    # 反转xy轴
    bar.reversal_axis()

    timeline.add(bar, str(year))

# for循环每一年的数据，基于每一年的数据，创建每一年的bar对象
# 在for中，将每一年的bar对象添加到时间线中
    
# 设置时间线自动播放
timeline.add_schema(
    play_interval=1000,
    is_auto_play=True,
    is_loop_play=False,
    is_timeline_show=True
)

# 绘图
timeline.render("1960-2019全球GDP前8国家.html")