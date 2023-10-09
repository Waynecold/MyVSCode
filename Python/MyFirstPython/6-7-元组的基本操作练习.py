# 定义一个元组记录学生的信息（姓名，年龄，爱好）
identity = ("Wayne", 30, ["coding", "video games"])
print(f"学生的信息是：{identity}")

# 查询其年龄所在的下标位置
num = identity.index(30)
print(f"年龄的下标是：{num}")

# 查询学生的姓名
name = identity[0]
print(f"姓名是：{name}")

# 删除学生爱好中的"video games"
identity[2].remove("video games")
print(f"学生的信息是：{identity}")

# 增加爱好"football"
identity[2].append("football")
print(f"学生的信息是：{identity}") 