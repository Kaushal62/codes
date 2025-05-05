from collections import deque

def dfs(graph,node,visited=None):
	if visited==None:
		visited=set()
	visited.add(node)
	print(node)
	for i in graph[node]:
		if i not in visited:
			dfs(graph,i,visited)

def bfs(graph,start):
	visited=set()
	queue=deque([start])
	visited.add(start)
	while queue:
		node=queue.popleft()
		print(node)
		for i in graph[node]:
			if i not in visited:
				visited.add(i)
				queue.append(i)



graph={}

n=int(input("enter"))

for i in range(n):
	node=int(input("enter name of "+ str(i+1) +" : "))
	neighbor=list(map(int,input("enter node connected to "+str(node)+" : ").split()))
	graph[node]=neighbor


start=int(input("enter start "))
print("dfs")
dfs(graph,start)

print("bfs")

bfs(graph,start)