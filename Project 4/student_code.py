import math

# Create custom class for storing map paths and calculating f values
class map_path():
    def __init__(self, m, node, goal, g=0, path=[]):
        # Set map and goal
        self.m = m
        self.goal = goal
        # Set g to given g
        self.g = g
        # Figure out what to do with path
        if path == []:
            self.path = [node]
        else:
            self.path = path
            
            # Increment g if this isn't the first node being added
            self.g += self.find_cost(self.get_last(), node)
            
            self.path.append(node)

        self.h = self.find_cost(self.get_last(), self.goal)
        self.f = self.g + self.h

    def add_node(self, number):
        return map_path(self.m, number, self.goal, self.g, self.path[:])

    def get_last(self):
        return self.path[-1]
    
    def find_cost(self, point_a, point_b):
        # Using this for point and goal gives h, but using this for point and next point gives g
        # I used euclidean distance heuristic function, as it made the most sense because of the constraints on movement in the map
        #
        # I looked into Manhatten distance and Diagonal distance heuristic functions, but both of those assumed there was a range of motion, 
        # in four or more directions.
        #
        # Given that each node only had a single path to each neighbor it had to follow, which was a straight line, and we were given the 
        # (x, y) coordinates of each node, euclidean distance was the most logical and straight-forward
        return math.sqrt( math.pow(self.m.intersections[point_b][0] - self.m.intersections[point_a][0], 2) + math.pow(self.m.intersections[point_b][1] - self.m.intersections[point_a][1], 2) )
    
    def __str__(self):
        return str(self.path) + " and f = " + str(self.f)



def shortest_path(m,start,goal):
    # Initialize the path
    best_path = map_path(m, start, goal)
    
    # Initialize the explored and frontier lists
    explored = []
    frontier = [best_path]
    
    # Now iterate
    while best_path.get_last() != goal or best_path.f >= frontier[0].f:
        best_path = frontier.pop(0)
        
        last_node = best_path.get_last()
        explored.append(last_node)

        for n in m.roads[last_node]:
            if n not in explored:
                new_path = best_path.add_node(n)
                if len(frontier) > 0:
                    i = 0
                    while i < len(frontier) and new_path.f > frontier[i].f:
                        i += 1
                    frontier.insert(i, new_path)
                else:
                    frontier.append(new_path)

    return best_path.path