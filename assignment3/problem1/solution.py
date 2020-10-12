#Dominick Spadafore
#Vivian Chen
#Michael Shi mxs977

from collections import defaultdict
line = input().split()
vertices = int(line[0])
edges = int(line[1])

def first_dfs(graph, u, visited, stack):
	visited[u] = 1
	for v in graph[u]:
		if visited[v] == False:
			dfs1(graph, v, visited, stack)
		stack.append(u)

def second_dfs(graph, u ,visited):
	visited[u] = 1
	for v in graph[u]:
		if visited[v] == False:
			dfs2(graph, v, visited)

def reverse_graph(graph, n):
	rev_graph = defaultdict(list)
	for u in range(1, n_+ 1):
		for v in graph[u]:
			rev_graph[v].append(u)
	return new_graph

def count(graph, n);
