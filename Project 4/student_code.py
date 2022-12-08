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
    
    class map_path():
        def __init__(self, node, g=0, path=[]):
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
                
            
            
            self.h = self.find_cost(self.get_last(), goal)
            self.f = self.g + self.h

        def add_node(self, number):
            return map_path(number, self.g, self.path[:])

        def get_last(self):
            return self.path[-1]
        
        def find_cost(self, point_a, point_b):
            # Using this for point and goal gives h, but using this for point and next point gives g
            return math.sqrt( math.pow(m.intersections[point_b][0] - m.intersections[point_a][0], 2) + math.pow(m.intersections[point_b][1] - m.intersections[point_a][1], 2) )
        
        def __str__(self):
            return str(self.path) + " and f = " + str(self.f)


    
    print("shortest path called")
  

    best_path = map_path(start)

    explored = [start]
    frontier = []
    all_paths = []

    # fill frontier with values
    for n in m.roads[start]:
        new_path = best_path.add_node(n)
        if len(frontier) > 0:
            i = 0
            while i < len(frontier) and new_path.f > frontier[i].f:
                i += 1
            frontier.insert(i, new_path)
        else:
                frontier.append(new_path)
                
    print("Current path's:", best_path.path, "f =", best_path.f)
    myprint(frontier)
    print("\n next iter \n")
    
    # Now iterate
    while best_path.get_last() != goal or best_path.f > frontier[0].f:
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
        print("Current path's:", best_path.path, "f =", best_path.f)
        myprint(frontier)
        print("\n next iter \n")
    
    print("\n\n Finished \n\n")
    return best_path.path

            
# def find_cost(m, point_a, point_b):
#     # Using this for point and goal gives h, but using this for point and next point gives g
#     print(m.intersections[0])
#     return math.sqrt( (m.intersections[point_b][0] - m.intersections[point_a][0])**2 + (m.intersections[point_b][1] - m.intersections[point_a][1])**2 )

def myprint(arr):
    output = "Frontier:\n"
    for mp in arr:
        output += str(mp)
        output += "\n"
    print(output)
        

    
    
    
    
    return


