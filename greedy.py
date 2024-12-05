import numpy as np  

# 计算贪心算法得到的路径和总距离  
def greedy_tsp(distance_matrix):  
    n = len(distance_matrix)  # 城市数量  
    visit_order = [0]  # 访问顺序，从城市0开始  
    visited = set(visit_order)  # 已访问的城市集  
    total_distance = 0  # 总距离初始化为0  

    # 贪心选择下一个最近的城市  
    for _ in range(1, n):  
        last_visited = visit_order[-1]  
        # 找到最近的未访问城市  
        next_city = min((distance_matrix[last_visited][j], j) for j in range(n) if j not in visited)[1]  
        visit_order.append(next_city)  # 添加到行程中  
        visited.add(next_city)  # 标记为已访问  
        total_distance += distance_matrix[last_visited][next_city]  # 更新总距离  

    # 回到起始城市  
    total_distance += distance_matrix[visit_order[-1]][visit_order[0]]  

    return visit_order, total_distance  

# 示例距离矩阵  
distance_matrix = np.array([  
    [0, 10, 15, 20],  
    [10, 0, 35, 25],  
    [15, 35, 0, 30],  
    [20, 25, 30, 0]  
])  

path, distance = greedy_tsp(distance_matrix)  

print("访问顺序:", path)  
print("总距离:", distance)