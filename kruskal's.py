class DsjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
    
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False

def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    ds = DsjointSet(vertices)
    mst = []
    total_weight = 0

    for u, v, w in edges:
        if ds.union(u, v):
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight

# Input
v_count = int(input("Number of vertices: "))
e_count = int(input("Number of edges: "))

vertices = set()
edges = []

print("Enter each edge in format: source destination weight")
for _ in range(e_count):
    u, v, w = input().split()
    w = int(w)
    vertices.update([u, v])
    edges.append((u, v, w))

mst, weight = kruskal(vertices, edges)

# Output
print("\nMinimum Spanning Tree (MST) Edges:")
for u, v, w in mst:
    print(f"{u} - {v}: {w}")
print(f"Total weight of MST: {weight}")



