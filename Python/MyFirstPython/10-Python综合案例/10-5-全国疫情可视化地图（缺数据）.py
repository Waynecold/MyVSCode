# 演示全国疫情可视化地图开发

import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

# 读取数据文件
f = open("D:/Documents/MyVSCode/Python/MyFirstPython/10-Python综合案例/10-5-1-疫情.txt", "r", encoding="utf-8")
data = f.read()

# 关闭文件
f.close()

# 取到各省数据
## 将字符串json转换为python的字典
data_dict = json.loads(data)
## 从字典中取出省份的数据
province_data_list = data_dict["areaTree"][0]["children"]
## 组装每个省份和确诊人数为元组（不可修改），并各个省份的数据都封装到列表内
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"] # 省份名称
    province_confirm = province_data["total"]["confirm"] # 确诊人数
    data_list.append((province_name, province_confirm)) # 追加到元组中

# 创建地图对象
map = Map()

# 添加数据
map.add("各省份确诊人数", data_list, "china")

# 设置全局
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"label":"1-99人","color":"#CCFFFF"},
            {"min":100,"max":999,"label":"100-999人","color":"#FFFF99"},
            {"min":1000,"max":4999,"label":"1000-4999人","color":"#FF9966"},
            {"min":5000,"max":9999,"label":"5000-9999人","color":"#FF6666"},
            {"min":10000,"max":99999,"label":"10000-99999人","color":"#CC3333"},
            {"min":100000,"label":"10000人以上","color":"#990033"},
        ]
    )
)

# 绘图
map.render("全国疫情地图.html") # 创建并命名目标文件