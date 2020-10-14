#Dominick Spadafore djs6744
#Vivian Chen vyc5073
#Michael Shi mxs977

from collections import defaultdict

# DFS for graph
def first_dfs(graph, v, visited, arr):
	visited[v] = True
	for e in graph[v]:
		if visited[e] == False:
			first_dfs(graph, e, visited, arr)
		arr.append(v)

# DFS for reversed graph
def second_dfs(graph, v ,visited):
	visited[v] = True
	for e in graph[v]:
		if visited[e] == False:
			second_dfs(graph, e, visited)

# Transposes the inputted graph and returns the reversed version
def reverse_graph(graph, vertices):
	new_graph = defaultdict(list)
	for i in range(0, vertices):
		for j in graph[i]:
			new_graph[j].append(i)
	return new_graph

# Function to count the connected components
def count(graph, vertices):
	arr = []
	count = 0
	reversed_graph = reverse_graph(graph, vertices)
	# Initializes all of the variables to not have been visited
	visited = [False] * (vertices + 1)
	for i in range(0, vertices):
		if visited[i] == False:
			first_dfs(graph, i, visited, arr)
	# Sets them all back to false for the second dfs through
	visited = [False] * (vertices + 1)
	while len(arr) != 0:
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