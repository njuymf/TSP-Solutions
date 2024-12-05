import itertools  

class TSP:  
    def __init__(self, distance_matrix):  
        self.distance_matrix = distance_matrix  # 城市间距离矩阵  
        self.num_cities = len(distance_matrix)  # 城市数量  
        self.memo = {}  # 用于存储子问题结果的字典  

    def tsp_dp(self, current_city, visited):  
        # 如果所有城市都已被访问，返回到起始城市的成本  
        if visited == (1 << self.num_cities) - 1:  
            return self.distance_matrix[current_city][0]  
        
        # 如果已计算过，返回存储的结果  
        if (current_city, visited) in self.memo:  
            return self.memo[(current_city, visited)]  
        
        # 初始化最小成本  
        min_cost = float('inf')  

        # 遍历所有城市，寻找下一个城市  
        for next_city in range(self.num_cities):  
            if visited & (1 << next_city) == 0:  # 如果城市未被访问  
                # 计算到下一个城市的成本  
                cost = self.distance_matrix[current_city][next_city] + self.tsp_dp(next_city, visited | (1 << next_city))  
                # 更新最小成本  
                min_cost = min(min_cost, cost)  

        # 存储结果并返回最小成本  
        self.memo[(current_city, visited)] = min_cost  
        return min_cost  

    def find_shortest_path(self):  
        # 从起始城市（0）出发，初始时只访问起始城市  
        return self.tsp_dp(0, 1 << 0)  # 1 << 0 表示只有起始城市被访问  


# 示例距离矩阵（城市间距离）  
distance_matrix = [  
    [0, 10, 15, 20],  
    [10, 0, 35, 25],  
    [15, 35, 0, 30],  
    [20, 25, 30, 0]  
]  

# 创建TSP对象并调用方法  
tsp = TSP(distance_matrix)  
min_cost = tsp.find_shortest_path()  

print("最小成本:", min_cost)