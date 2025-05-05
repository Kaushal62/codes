

def prims_algorithm(graph, vertices):
    selected = [False] * vertices
    selected[0] = True  # Start from the first vertex
    print("Edge : Weight")

    for _ in range(vertices - 1):
        min_weight =99999999999999999999
        u = v = 0
        for i in range(vertices):
            if selected[i]:
                for j in range(i + 1, vertices):  # Only iterate for the upper triangle
                    if (not selected[j]) and graph[i][j]:
                        if min_weight > graph[i][j]:
                            min_weight = graph[i][j]
                            u, v = i, j
        print(chr(97 + u) + " - " + chr(97 + v) + " : " + str(graph[u][v]))
        selected[v] = True

# Input from user
vertices = int(input("Enter number of vertices: "))
graph = [[0] * vertices for _ in range(vertices)]
print(graph)

print("Enter adjacency matrix upper triangle row by row (0 if no edge):")
for i in range(vertices):
    for j in range(i + 1, vertices):
        weight = int(input("Enter weight for edge " + chr(97 + i) + " - " + chr(97 + j) + ": "))
        graph[i][j] = weight
        graph[j][i] = weight  # fill symmetric value

# Print the graph (adjacency matrix)
print("\nAdjacency Matrix:")
for row in graph:
    for val in row:
        print(str(val) + "\t", end="")
    print()


# Run Prim's Algorithm
print()
prims_algorithm(graph, vertices)
