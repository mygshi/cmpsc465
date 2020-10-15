#Dominick Spadafore djs6744
#Vivian Chen vyc5073
#Michael Shi mxs977

def find_min(dist, prev):

        min = 999999
        index = 0

        for v in range(n):
            if dist[v] < min and prev[v] == None:
                min = dist[v]
                index = v

        return index

def dijkstra(s, n, graph): 

    dist = [999999] * n
    dist[s] = 0
    prev = [None] * n 
  
    for cout in range(n): 
  
        u = find_min(dist, prev)
  
        prev[u] = True
  
        for v in range(n): 
            if graph[u][v] > 0 and prev[v] == None and dist[v] > dist[u] + graph[u][v]: 
                dist[v] = dist[u] + graph[u][v]
  
    for i in range(n):
        if(dist[i] == 999999):
            dist[i] = -1
        print(dist[i])

# Mainframe
line1 = input().split()
n = int(line1[0])
m = int(line1[1])
s = int(line1[2])
graph = []
for i in range(0, n):
    graph.append([0]*n)

for i in range(0, m):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])
    graph[a-1][b-1] = c

dijkstra(s-1, n, graph)
