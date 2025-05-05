import heapq

graph = {}
heuristic = {}

# Taking input for the graph
n = int(input("Enter number of vertices: "))

for _ in range(n):
    vertex = input("\nEnter vertex name: ")
    graph[vertex] = []
    neighbors = int(input("Enter number of neighbors of " + vertex + ": "))
    
    for _ in range(neighbors):
        neighbor = input("Enter neighbor name: ")
        weight = int(input("Enter weight from " + vertex + " to " + neighbor + ": "))
        graph[vertex].append((neighbor, weight))
print("\nGraph:", graph)

# Taking input for heuristic values
print("\nEnter heuristic values for each vertex:")
for vertex in graph:
    h = int(input("Heuristic for " + vertex + ": "))
    heuristic[vertex] = h

# A* Algorithm
def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], 0, start, [start]))
    closed_set = set()
    
    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        
        if current == goal:
            print("\nPath:", ' -> '.join(path))
            print("Cost:", g) 
            return
        
        closed_set.add(current)
        
        for neighbor, cost in graph[current]:
            if neighbor not in closed_set:
                total_g = g + cost
                total_f = total_g + heuristic[neighbor] 
                heapq.heappush(open_list, (total_f, total_g, neighbor, path + [neighbor]))
    
    print("\nNo path found!")

# Run A* Algorithm
start_node = input("\nEnter start node: ")
goal_node = input("Enter goal node: ")

a_star(start_node, goal_node)
