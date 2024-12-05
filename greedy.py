class TSP:  
    def __init__(self, distance_matrix):  
        self.distance_matrix = distance_matrix  # 城市间距离矩阵  
        self.num_cities = len(distance_matrix)  # 城市数量  
        self.best_path = None  # 最佳路径  
        self.min_cost = float('inf')  # 初始化最小成本为无穷大  

    def backtrack(self, current_position, visited, current_cost, path):  
        # 如果所有城市都已访问，检查是否返回起始城市的总费用  
        if len(visited) == self.num_cities:  
            cost_to_start = self.distance_matrix[current_position][0]  
            total_cost = current_cost + cost_to_start  
            if total_cost < self.min_cost:  
                self.min_cost = total_cost  
                self.best_path = path + [0]  # 回到起始城市  
            return  
        
        # 递归访问每一个城市  
        for next_city in range(self.num_cities):  
            if next_city not in visited:  
                next_cost = current_cost + self.distance_matrix[current_position][next_city]  
                self.backtrack(next_city, visited | {next_city}, next_cost, path + [next_city])  

    def find_shortest_path(self):  
        # 从起始城市（0）出发，开始回溯法  
        self.backtrack(0, {0}, 0, [0])  
        return self.best_path, self.min_cost  


# 示例距离矩阵（城市间距离）  
distance_matrix = [  
    [0, 10, 15, 20],  
    [10, 0, 35, 25],  
    [15, 35, 0, 30],  
    [20, 25, 30, 0]  
]  

# 创建TSP对象并调用方法  
tsp = TSP(distance_matrix)  
shortest_path, min_cost = tsp.find_shortest_path()  

print("最优路径:", shortest_path)  
print("最小成本:", min_cost)