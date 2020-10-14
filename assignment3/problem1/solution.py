#Dominick Spadafore
#Vivian Chen
#Michael Shi mxs977

from collections import defaultdict

# DFS for graph
def first_dfs(graph, u, visited, stack):
	visited[u] = True
	for v in graph[u]:
		if visited[v] == False:
			first_dfs(graph, v, visited, stack)
		stack.append(u)

# DFS for reversed graph
def second_dfs(graph, u ,visited):
	visited[u] = True
	for v in graph[u]:
		if visited[v] == False:
			second_dfs(graph, v, visited)

# Transposes the inputted graph and returns the reversed version
def reverse_graph(graph, vertices):
	new_graph = defaultdict(list)
	for u in range(0, vertices):
		for v in graph[u]:
			new_graph[v].append(u)
	return new_graph

# Function to count the connected components
def count(graph, vertices):
	arr = []
	count = 0
	reversed_graph = reverse_graph(graph, vertices)
	visited = [False] * (vertices + 1)
	for i in range(0, vertices):
		if visited[i] == False:
			first_dfs(graph, i, visited, arr)
	visited = [False] * (vertices + 1)
	while len(arr) > 0:
		last_element = arr.pop()
		if visited[last_element] == False:
			count += 1
			second_dfs(reversed_graph, last_element, visited)
	return count

# Main
line1 = input().split()
vertices = int(line1[0])
edges = int(line1[1])
graph = defaultdict(list)

for i in range(0, edges):
	line = input().split()
	u = int(line[0])
	v = int(line[1])
	graph[u].append(v)

print(count(graph, vertices))