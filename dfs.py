from collections import deque
       
def dfs(graph,node,visited=None):
	if visited == None:
		visited=set()
	visited.add(node)
	print(node,end=" ")
	for i in graph[node]:
		if i not in visited:
			dfs(graph,i,visited)
            
def bfs(graph,start):
	visited=set()
	queue=deque([start])
	visited.add(start)

	
	while queue:
		node=queue.popleft()
		print(node,end=" ")
		for i in graph[node]:
			if i not in visited:
				visited.add(i)
				queue.append(i)



graph={}

n=int(input("Enter the number of vertices : "))

for i in range(n):
	node=int(input("Enter node"+str(i+1)+" : "))
	node_n=list(map(int,input("Enter node connected to "+str(node)+ " : " ).split()))
	graph[node]=node_n

start_node=int(input("Enter the starting node : "))

dfs(graph,start_node)

print("\n")
bfs(graph,start_node)