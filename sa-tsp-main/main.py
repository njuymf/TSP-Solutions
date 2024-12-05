
import numpy as np
import config as conf
from sa import Sa
import matplotlib.pyplot as plt

config = conf.get_config()

def build_dist_mat(input_list):
    n = config.city_num
    dist_mat = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            d = input_list[i, :] - input_list[j, :]
            dist = np.linalg.norm(d)
            dist_mat[i, j] = dist
            dist_mat[j, i] = dist
    return dist_mat

# 生成随机城市坐标
city_pos_list = np.random.rand(config.city_num, config.pos_dimension)
# 计算城市距离矩阵
city_dist_mat = build_dist_mat(city_pos_list)

print("城市坐标：")
print(city_pos_list)
print("城市距离矩阵：")
print(city_dist_mat)

# 退火算法运行
sa = Sa(city_dist_mat)
best_solution, distance_list = sa.train()
best_solution.append(best_solution[0])  # 回到起点
result_pos_list = city_pos_list[best_solution, :]

# 绘图
plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 创建两个子图
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# 左侧子图：绘制最佳路线
ax[0].plot(result_pos_list[:, 0], result_pos_list[:, 1], 'o-r')
ax[0].set_title("最佳路线")

# 右侧子图：绘制距离变化曲线
ax[1].plot(distance_list)
ax[1].set_title("距离变化曲线")

# 调整布局并显示
plt.tight_layout()
plt.show()

