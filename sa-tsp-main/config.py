
def get_config():
    class Config:
        # 遗传算法参数
        city_num = 20             # 城市数量
        pos_dimension = 2         # 坐标维度
        individual_num = 1000      # 种群数量
        gen_num = 500             # 迭代代数
        mutate_prob = 0.05        # 变异概率

        # 退火算法参数
        T0 = 1000                 # 初始温度
        T_end = 0.1                 # 终止温度
        L = 500                   # 每个温度下的迭代次数
        alpha = 0.98              # 降温系数

    return Config()

