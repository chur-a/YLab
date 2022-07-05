from itertools import permutations
from typing import List, Tuple

def short_path(points: List[Tuple[int, int]]):
    starting_point = points[0]
    points = points[1:]
    path = []
    path_length = float('inf')
    
    def calc_distance(point_1, point_2):
        return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5
    
    for inst_path in permutations(points):
        inst_length = calc_distance(starting_point, inst_path[0])
        check = [starting_point, [inst_path[0], inst_length]]
        for i in range(1, len(inst_path)):
            inst_length += calc_distance(inst_path[i], inst_path[i-1])
            check.append([inst_path[i], inst_length])
        inst_length += calc_distance(inst_path[-1], starting_point)
        check.append([starting_point, inst_length])
        if inst_length < path_length:
            path, path_length = check, inst_length
    return path, path_length


print(short_path([(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]))

