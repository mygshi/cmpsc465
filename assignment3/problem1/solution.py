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
	for i in range(1, vertices + 1):
		for j in graph[i]:
			new_graph[j].append(i)
	return new_graph

# Function to count the connected components
def count(graph, vertices):
	# Initializes the array, count, and creates a reversed graph of the inputted one
	arr = []
	count = 0
	reversed_graph = reverse_graph(graph, vertices)
	# Initializes all of the variables to not have been visited
	visited = [False] * (vertices + 1)
	# Goes through all of the vertices and checks if they have been visited already, if it has it then runs a dfs on it and keeping track of what has been visited
	for i in range(1, vertices + 1):
		if visited[i] == False:
			first_dfs(graph, i, visited, arr)
	# Sets them all back to false for the second dfs through
	visited = [False] * (vertices + 1)
	# Goes through the array of visited elements, pops the first one and checks if it is visited. If it is not, that means it is a connected component and adds to the count before 
	# going through the second dfs
	while len(arr) != 0:
		last_element = arr.pop()
		if visited[last_element] == False:
			count += 1
			second_dfs(reversed_graph, last_element, visited)
	return count

# Main
# Takes in the first line of input from the file, and creates the graph using a dictionary
line1 = input().split()
vertices = int(line1[0])
edges = int(line1[1])
graph = defaultdict(list)

# Goes through all of the edges and appends the edges into the corresponding vertex
for i in range(0, edges):
	line = input().split()
	u = int(line[0])
	v = int(line[1])
	graph[u].append(v)

# Goes through the count function and prints out the result 
print(count(graph, vertices))