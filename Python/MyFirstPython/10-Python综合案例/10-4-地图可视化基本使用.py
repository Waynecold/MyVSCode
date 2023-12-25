# 演示地图可视化的基本使用
from pyecharts.charts import Map # 导入创建地图功能
from pyecharts.options import VisualMapOpts # 导入可视化地图设置功能
# 准备地图对象
map = Map()

# 准备数据
data = [
    ("北京市", 1),
    ("上海市", 9),
    ("湖南省", 19),
    ("台湾省", 199),
    ("广东省", 299),
]

# 添加数据
map.add("测试地图", data, "china")

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True, # 显示颜色
        is_piecewise=True, # 手动设置分段
        pieces=[
            {"min":1, "max":9, "label":"1-9人", "color":"#CCFFFF"},
            {"min":10, "max":99, "label":"10-99人", "color":"#FF6666"},
            {"min":100, "max":500, "label":"100-500人", "color":"#990033"},
        ]
    )
)

# 绘图
map.render("地图可视化基本使用.html")