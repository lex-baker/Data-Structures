import math

"""
all_paths= [] # a bunch of whats below, ordered by f
current path = 
[
    [1, 4, 2, 7],   # Path
    42             # F total

]

"""


def shortest_path(m,start,goal):

    class map_node():
        def __init__(self, number):
            self.number = number
            self.g = 0
            self.h = math.sqrt( (m.intersections[goal][0] - m.intersections[number][0])**2 + (m.intersections[goal][1] - m.intersections[number][1])**2 )

        def f(self):
            return self.g + self.h

    class map_path():
        def __init__(self, next, g, path):
            if path:
                self.path = path
                self.path.append(next)
            else:
                self.path = [next]
            self.g = g or 0
            self.h = find_cost(self.get_last, goal)
            self.total_f = self.g + self.h

        def add_node(self, number):
            self.path.append(number)
            return map_path(number, self.path[:])

        def get_last(self):
            return self.path[-1]

        def f(self):
            return self.total_f


    
    print("shortest path called")
  

    first_path = map_path(start)
    print(first_path.total_g)


    explored = []
    frontier = [map_node(start)]
    all_paths = []

    while True:
        path = frontier.pop(0)
        explored.append(path.get_last())

        for n in m.roads[node]:
            if n not in explored:

            
        


    
    
    
    
    return

def find_cost(map, point_a, point_b):
    # Using this for point and goal gives h, but using this for point and next point gives g
    return math.sqrt(map.intersections[point_a]**2 + map.intersections[point_b]**2)
