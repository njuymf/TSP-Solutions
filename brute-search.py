import itertools  

def calculate_distance(path, distance_matrix):  
    """计算给定路径的总距离"""  
    total_distance = 0  
    for i in range(len(path) - 1):  
        total_distance += distance_matrix[path[i]][path[i + 1]]  
    total_distance += distance_matrix[path[-1]][path[0]]  # 返回到起始城市  
    return total_distance  

def tsp_brute_force(distance_matrix):  
    """使用暴力搜索解决旅行商问题"""  
    n = len(distance_matrix)  
    cities = list(range(n))  # 城市列表  
    min_distance = float('inf')  
    best_path = []  

    # 生成所有可能的城市顺序  
    for path in itertools.permutations(cities):  
        current_distance = calculate_distance(path, distance_matrix)  
        if current_distance < min_distance:  
            min_distance = current_distance  
            best_path = path  

    return best_path, min_distance  

# 示例：使用城市间距离矩阵进行测试  
if __name__ == "__main__":  
    distance_matrix = [  
        [0, 10, 15, 20],  
        [10, 0, 35, 25],  
        [15, 35, 0, 30],  
        [20, 25, 30, 0]  
    ]  
    
    best_path, min_distance = tsp_brute_force(distance_matrix)  
    print("最短路径:", best_path)  
    print("最短距离:", min_distance)