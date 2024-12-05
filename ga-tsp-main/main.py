import numpy as np  
import config as conf  
from ga import Ga  
import matplotlib.pyplot as plt  

config = conf.get_config()  


def build_dist_mat(input_list):  
    n = config.city_num  
    dist_mat = np.zeros([n, n])  
    for i in range(n):  
        for j in range(i + 1, n):  
            d = input_list[i, :] - input_list[j, :]  
            dist_mat[i, j] = np.dot(d, d)  
            dist_mat[j, i] = dist_mat[i, j]  
    return dist_mat  


# 城市坐标  
city_pos_list = np.random.rand(config.city_num, config.pos_dimension)  
# 城市距离矩阵  
city_dist_mat = build_dist_mat(city_pos_list)  

print(city_pos_list)  
print(city_dist_mat)  

# 遗传算法运行  
ga = Ga(city_dist_mat)  
result_list, fitness_list = ga.train()  
result = result_list[-1]  
result_pos_list = city_pos_list[result, :]  

# 绘图  
# 解决中文显示问题  
plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体  
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题  

# 创建一个包含两个子图的图形  
fig, ax = plt.subplots(1, 2, figsize=(12, 6))  

# 左侧子图: 绘制路线  
ax[0].plot(result_pos_list[:, 0], result_pos_list[:, 1], 'o-r')  
ax[0].set_title(u"路线")  
ax[0].legend()  

# 右侧子图: 绘制适应度曲线  
ax[1].plot(fitness_list)  
ax[1].set_title(u"适应度曲线")  
ax[1].legend()  

# 调整布局  
plt.tight_layout()  
plt.show()