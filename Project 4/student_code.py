import math

class map_node():
    m = None
    def __init__(self, node):
        self.node = node
        self.g = 0
        self.h = 

class map_path():
    m = None
    def __init__(self, start):


def shortest_path(m,start,goal):
    print("shortest path called")
    
    map_node.m = m

    explored = []
    frontier = [start]
    unexplored = [] # Maybe not, idk yet

    while True:
        node = frontier.pop(0)
        explored.append(node)

        for n in m.roads[node]:
            
        


    
    
    
    
    return

def find_cost(map, point_a, point_b):
    return math.sqrt(map.intersections[point_a]**2 + map.intersections[point_b]**2)
