
import config as conf
import random
import numpy as np
from typing import List

config = conf.get_config()

# 参数配置
initial_temperature = config.T0       # 初始温度
final_temperature = config.T_end      # 终止温度
cooling_rate = config.alpha           # 降温系数
iterations_per_temp = config.L        # 每个温度下的迭代次数
city_dist_mat = None


def copy_list(old_arr: List[int]):
    return old_arr.copy()


# 退火算法类
class Sa:
    def __init__(self, dist_mat):
        global city_dist_mat
        city_dist_mat = dist_mat
        self.city_num = dist_mat.shape[0]
        self.best_solution = None
        self.best_distance = float('inf')
        self.distance_list = []

    def initial_solution(self):
        solution = list(range(self.city_num))
        random.shuffle(solution)
        return solution

    def calculate_distance(self, solution):
        distance = 0.0
        for i in range(self.city_num - 1):
            distance += city_dist_mat[solution[i], solution[i + 1]]
        distance += city_dist_mat[solution[-1], solution[0]]  # 回到起点
        return distance

    def get_neighbor(self, solution):
        new_solution = copy_list(solution)
        # 选择两个不同的城市进行交换
        a, b = random.sample(range(self.city_num), 2)
        new_solution[a], new_solution[b] = new_solution[b], new_solution[a]
        return new_solution

    def train(self):
        current_solution = self.initial_solution()
        current_distance = self.calculate_distance(current_solution)
        self.best_solution = copy_list(current_solution)
        self.best_distance = current_distance
        self.distance_list.append(self.best_distance)
        temperature = initial_temperature

        while temperature > final_temperature:
            for _ in range(iterations_per_temp):
                candidate_solution = self.get_neighbor(current_solution)
                candidate_distance = self.calculate_distance(candidate_solution)
                delta = candidate_distance - current_distance

                if delta < 0 or random.random() < np.exp(-delta / temperature):
                    current_solution = candidate_solution
                    current_distance = candidate_distance

                    if current_distance < self.best_distance:
                        self.best_solution = copy_list(current_solution)
                        self.best_distance = current_distance
                        self.distance_list.append(self.best_distance)
            temperature *= cooling_rate

        return self.best_solution, self.distance_list

